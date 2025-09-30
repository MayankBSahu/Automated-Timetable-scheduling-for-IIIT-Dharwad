# very small exporter that writes a simple CSV of sessions
import csv
from typing import List
from .models import Course

def export_sessions_csv(courses: List[Course], path: str):
    rows = []
    for c in courses:
        for s in c.sessions:
            rows.append({
                'courseCode': c.courseCode,
                'courseName': c.courseName,
                'day': s.day,
                'time': s.time,
                'slot': s.slot,
                'room': s.room,
                'type': s.type
            })
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ['courseCode','courseName','day','time','slot','room','type'])
        writer.writeheader()
        writer.writerows(rows)
    print('Wrote CSV to', path)
