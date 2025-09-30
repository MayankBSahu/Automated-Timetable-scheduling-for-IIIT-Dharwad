# Automated-Timetable-scheduling-for-IIIT-Dharwad
Creating an 'Automated Timetable scheduling' for IIIT Dharwad
timetable-automation/
│── config/                # Configuration files (Python for slots, rules, constraints)
│   ├── slots.json
│   ├── rules.json
│   └── database_config.json
│
│── data/                  # Input/output data
│   ├── timetable_aug_dec_2025.json   # Generated from your provided images
│   ├── sample_input.json
│   └── output_timetable.json
│
│── src/                   # Core source code
│   ├── __init__.py
│   ├── main.py            # Entry point
│   ├── scheduler.py       # Algorithm for timetable generation
│   ├── validator.py       # Conflict detection & validation
│   ├── visualizer.py      # Generate color-coded timetables
│   ├── exporter.py        # Export to PDF, Excel, Google Calendar
│   └── database.py        # Data persistence (save/load Python or DB)
│
│── models/                # Data structures (mapped from PDF Low-Level Design)
│   ├── faculty.py
│   ├── course.py
│   ├── room.py
│   ├── exam.py
│   └── timetable.py
│
│── tests/                 # Unit tests
│   ├── test_scheduler.py
│   └── test_validator.py
│
│── requirements.txt       # Python dependencies (pandas, matplotlib, etc.)
│── README.md              # Documentation

