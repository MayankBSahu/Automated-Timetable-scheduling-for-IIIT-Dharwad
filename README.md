# Automated-Timetable-scheduling-for-IIIT-Dharwad
Creating an 'Automated Timetable scheduling' for IIIT Dharwad
# Timetable Automation (minimal Python implementation)

This repository contains a minimal implementation of the DPR-specified
timetable automation system. It provides:
- dataclass models for Course/Session/Faculty/Room/Student
- a JSON loader/saver
- basic validators for faculty and student conflicts
- a scheduler class with simple helpers
- a visualizer that can print and plot a day's timetable
- an exporter to CSV

## How to run (local)
```bash
python -m pip install -r requirements.txt
python cli.py --data sample_data/timetable_aug_dec_2025.json
```

## What I implemented
This is a starting point — the real scheduling algorithm (GA/ILP etc.)
is not implemented here. The modules are organized to make that
integration straightforward.

