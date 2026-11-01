# Program Monitor Reports

One file per run of the [monthly program monitor](../../../../.github/workflows/monthly-monitor.yml) (CA-7, evidence E-25), named by the date it ran (`2026-12-01.md`). Each is committed by `github-actions[bot]` and holds:

  - the due-date report from [`tools/due_dates.py`](../../../../tools/due_dates.py): overdue items, items due in the next 30 days, and recurring activities that are behind
  - the full consistency checker result across all three repositories
  - a link to the workflow run that produced it

The reports **read** the program's records and change nothing else. They never mark an activity as done: a missed date stays in every report until someone does the work and records it in the right log.

The same report is posted as a "Program monitor" issue (label `program-monitor`) when the workflow runs on `main`.

---

*This document is a simulation for educational and portfolio purposes only.*
