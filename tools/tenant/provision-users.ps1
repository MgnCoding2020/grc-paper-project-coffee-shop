<#
.SYNOPSIS
    Creates Burn and Churn Coffee users and groups in Microsoft Entra ID from people.csv.

.DESCRIPTION
    Reads the canonical roster (00-company-profile/org/people.csv) and, for every person
    who is not terminated:
      - creates the user (if missing) with department "Burn and Churn Coffee" and a random
        temporary password that must be changed at first sign-in
      - creates each grp-bc-* security group listed in the roster (if missing)
      - adds the user to their groups (if not already a member)

    It also reads vendor-contacts.csv and, for each contact whose status is Approved or Active,
    invites them as a B2B guest (if not already present) and adds them to their groups
    (grp-bc-vendors). Contacts that are Planned or Removed are skipped. The guest's real email
    address is read from .env (the key named in the contact's env_email_key column), never
    from a tracked file.

    Safe to run more than once: existing users, guests, groups and memberships are skipped.

    The fictional domain in people.csv (burnandchurncoffee.com) is swapped for the real
    tenant domain read from the git-ignored .env file at the hub root. Nothing tenant-specific
    is ever written to tracked files.

    Outputs (both in the git-ignored _raw/ folder):
      - initial-passwords-<timestamp>.csv  temporary passwords; hand out, then delete
      - provisioning-log-<timestamp>.csv   what was created or skipped, using the fictional
                                           domain only, so a copy can be committed as evidence

    Out of scope (deliberate manual steps, reviewed for least privilege): admin roles,
    adm- accounts, break-glass accounts, licences and MFA.

.PARAMETER DryRun
    Show what would be created without connecting to Microsoft Graph or changing anything.

.EXAMPLE
    .\tools\tenant\provision-users.ps1 -DryRun

.EXAMPLE
    .\tools\tenant\provision-users.ps1
#>
[CmdletBinding()]
param(
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$HubRoot   = Resolve-Path (Join-Path $PSScriptRoot '..\..')
$PeopleCsv   = Join-Path $HubRoot '00-company-profile\org\people.csv'
$ContactsCsv = Join-Path $HubRoot '00-company-profile\org\vendor-contacts.csv'
$EnvFile     = Join-Path $HubRoot '.env'
$RawDir    = Join-Path $HubRoot '_raw'
$Company   = 'Burn and Churn Coffee'
$Stamp     = Get-Date -Format 'yyyy-MM-dd-HHmmss'

function Read-DotEnv([string]$Path) {
    if (-not (Test-Path $Path)) {
        throw "Missing $Path. Copy .env.example to .env and fill in the tenant values."
    }
    $values = @{}
    foreach ($line in Get-Content $Path) {
        if ($line -match '^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$') { $values[$Matches[1]] = $Matches[2] }
    }
    foreach ($key in 'ENTRA_TENANT_ID', 'ENTRA_TENANT_DOMAIN', 'BC_DOC_DOMAIN') {
        if (-not $values[$key]) { throw "$key is not set in $Path." }
    }
    return $values
}

function New-TempPassword {
    # 16 characters with at least one upper, lower, digit and symbol, from a crypto RNG
    $sets = 'ABCDEFGHJKLMNPQRSTUVWXYZ', 'abcdefghijkmnopqrstuvwxyz', '23456789', '!@#$%*?-+='
    $all  = -join $sets
    $rng  = New-Object System.Security.Cryptography.RNGCryptoServiceProvider
    $bytes = New-Object byte[] 16
    $rng.GetBytes($bytes)
    $chars = for ($i = 0; $i -lt 16; $i++) {
        if ($i -lt 4) { $set = $sets[$i] } else { $set = $all }
        $set[$bytes[$i] % $set.Length]
    }
    return -join ($chars | Sort-Object { Get-Random })
}

$envValues  = Read-DotEnv $EnvFile
$docDomain  = $envValues['BC_DOC_DOMAIN']
$realDomain = $envValues['ENTRA_TENANT_DOMAIN']

# @() keeps these as arrays in PowerShell 5.1 even when only one row matches
$people = @(Import-Csv $PeopleCsv | Where-Object { $_.employment_status -ne 'Terminated' })
$skipped = @(Import-Csv $PeopleCsv | Where-Object { $_.employment_status -eq 'Terminated' })
$allContacts = @(Import-Csv $ContactsCsv)
$guests = @($allContacts | Where-Object { $_.status -in 'Approved', 'Active' })
$waiting = @($allContacts | Where-Object { $_.status -notin 'Approved', 'Active' })
$groupNames = @((@($people | ForEach-Object { $_.groups -split ';' }) + @($guests | ForEach-Object { $_.access_groups -split ';' })) |
    Where-Object { $_ } | Sort-Object -Unique)

Write-Host "Burn and Churn provisioning from people.csv and vendor-contacts.csv"
Write-Host ("  {0} people to provision, {1} terminated (skipped), {2} guests to invite, {3} groups" -f $people.Count, $skipped.Count, $guests.Count, $groupNames.Count)
foreach ($p in $skipped) { Write-Host "  skip  $($p.display_name) (Terminated: no account is created)" }
foreach ($c in $waiting) { Write-Host "  skip  $($c.contact_id) $($c.display_name) (vendor contact, status $($c.status): not invited)" }

if ($DryRun) {
    Write-Host ""
    Write-Host "DRY RUN: no connection to Microsoft Graph, nothing is changed."
    foreach ($g in $groupNames) { Write-Host "  group  $g" }
    foreach ($p in $people) {
        Write-Host ("  user   {0,-16} {1,-14} {2}  -> {3}" -f $p.display_name, $p.role, $p.upn, $p.groups)
    }
    foreach ($c in $guests) {
        Write-Host ("  guest  {0} {1} ({2}), access {3} to {4}  -> {5}" -f $c.contact_id, $c.display_name, $c.vendor_id, $c.access_start, $c.access_end, $c.access_groups)
    }
    Write-Host ""
    Write-Host "Real UPNs and guest email addresses come from .env; they are not printed here."
    return
}

$modules = 'Microsoft.Graph.Authentication', 'Microsoft.Graph.Users', 'Microsoft.Graph.Groups'
$scopes = 'User.ReadWrite.All', 'Group.ReadWrite.All'
if ($guests.Count) {
    $modules += 'Microsoft.Graph.Identity.SignIns'
    $scopes += 'User.Invite.All'
}
foreach ($module in $modules) {
    if (-not (Get-Module -ListAvailable $module)) {
        throw "Module $module is not installed. Run: Install-Module Microsoft.Graph -Scope CurrentUser"
    }
}

Connect-MgGraph -TenantId $envValues['ENTRA_TENANT_ID'] -Scopes $scopes -NoWelcome
New-Item -ItemType Directory -Force $RawDir | Out-Null
$log = New-Object System.Collections.Generic.List[object]
$passwords = New-Object System.Collections.Generic.List[object]

function Write-Log($Action, $Object, $Detail) {
    $entry = [pscustomobject]@{ timestamp = (Get-Date -Format 's'); action = $Action; object = $Object; detail = $Detail }
    $log.Add($entry)
    Write-Host ("  {0,-8} {1} {2}" -f $Action, $Object, $Detail)
}

# Groups
$groups = @{}
foreach ($name in $groupNames) {
    $existing = Get-MgGroup -Filter "displayName eq '$name'"
    if ($existing) {
        $groups[$name] = $existing | Select-Object -First 1
        Write-Log 'exists' $name 'group'
    } else {
        $groups[$name] = New-MgGroup -DisplayName $name -MailEnabled:$false -SecurityEnabled -MailNickname $name `
            -Description "$Company - $name"
        Write-Log 'created' $name 'security group'
    }
}

# Users and memberships
foreach ($p in $people) {
    $upn = $p.upn -replace [regex]::Escape("@$docDomain"), "@$realDomain"
    $user = Get-MgUser -Filter "userPrincipalName eq '$upn'" -ErrorAction SilentlyContinue
    if ($user) {
        Write-Log 'exists' $p.upn 'user'
    } else {
        $password = New-TempPassword
        $first, $last = $p.display_name -split ' ', 2
        $user = New-MgUser -DisplayName $p.display_name -GivenName $first -Surname $last `
            -UserPrincipalName $upn -MailNickname ($upn.Split('@')[0]) -AccountEnabled `
            -Department $Company -CompanyName $Company -JobTitle $p.role -UsageLocation 'US' `
            -PasswordProfile @{ Password = $password; ForceChangePasswordNextSignIn = $true }
        $passwords.Add([pscustomobject]@{ display_name = $p.display_name; upn = $upn; temporary_password = $password })
        Write-Log 'created' $p.upn "user ($($p.role))"
    }
    foreach ($name in ($p.groups -split ';' | Where-Object { $_ })) {
        $members = Get-MgGroupMember -GroupId $groups[$name].Id -All | Select-Object -ExpandProperty Id
        if ($members -contains $user.Id) {
            Write-Log 'exists' $p.upn "member of $name"
        } else {
            New-MgGroupMember -GroupId $groups[$name].Id -DirectoryObjectId $user.Id
            Write-Log 'added' $p.upn "to $name"
        }
    }
}

# Vendor guests (B2B invitations); logged by contact ID so the log never holds a real address
foreach ($c in $guests) {
    $email = $envValues[$c.env_email_key]
    if (-not $email) { throw "$($c.env_email_key) is not set in .env (email for vendor contact $($c.contact_id))." }
    $guest = Get-MgUser -Filter "mail eq '$email'" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($guest) {
        Write-Log 'exists' $c.contact_id "guest ($($c.display_name))"
    } else {
        $invite = New-MgInvitation -InvitedUserEmailAddress $email -InvitedUserDisplayName $c.display_name `
            -InviteRedirectUrl 'https://myapps.microsoft.com' -SendInvitationMessage:$true
        $guest = Get-MgUser -UserId $invite.InvitedUser.Id
        Write-Log 'invited' $c.contact_id "guest ($($c.display_name), $($c.vendor_id); access $($c.access_start) to $($c.access_end))"
    }
    foreach ($name in ($c.access_groups -split ';' | Where-Object { $_ })) {
        $members = Get-MgGroupMember -GroupId $groups[$name].Id -All | Select-Object -ExpandProperty Id
        if ($members -contains $guest.Id) {
            Write-Log 'exists' $c.contact_id "member of $name"
        } else {
            New-MgGroupMember -GroupId $groups[$name].Id -DirectoryObjectId $guest.Id
            Write-Log 'added' $c.contact_id "to $name"
        }
    }
}

$logPath = Join-Path $RawDir "provisioning-log-$Stamp.csv"
$log | Export-Csv $logPath -NoTypeInformation -Encoding UTF8
Write-Host ""
Write-Host "Log (fictional domain only, safe to review for evidence): $logPath"
if ($passwords.Count) {
    $pwPath = Join-Path $RawDir "initial-passwords-$Stamp.csv"
    $passwords | Export-Csv $pwPath -NoTypeInformation -Encoding UTF8
    Write-Host "Temporary passwords: $pwPath"
    Write-Host "  This file is git-ignored. Hand the passwords out, then delete it."
}
Disconnect-MgGraph | Out-Null
