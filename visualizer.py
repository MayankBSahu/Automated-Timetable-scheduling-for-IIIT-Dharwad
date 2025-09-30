from typing import List
from .models import Course
import matplotlib.pyplot as plt

def print_timetable(courses: List[Course]):
    print('Timetable summary:')
    for c in courses:
        print(f"{c.courseCode}: {c.courseName}")
        for s in c.sessions:
            print(f"  {s.day} {s.time} {s.slot} {s.room} ({s.type})")

def plot_day_timetable(courses: List[Course], day: str, out_path=None):
    # Very simple horizontal bar chart per session (one chart per call)
    items = []
    labels = []
    for c in courses:
        for s in c.sessions:
            if s.day == day:
                start = int(s.time.split('-')[0].split(':')[0])*60 + int(s.time.split('-')[0].split(':')[1])
                end = int(s.time.split('-')[1].split(':')[0])*60 + int(s.time.split('-')[1].split(':')[1])
                items.append((start, end-start))
                labels.append(f"{c.courseCode} ({s.room})")
    if not items:
        print('No sessions on', day)
        return None
    fig, ax = plt.subplots(figsize=(10, max(2, len(items)*0.5)))
    y = range(len(items))
    starts = [i[0] for i in items]
    widths = [i[1] for i in items]
    ax.barh(y, widths, left=starts)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel('minutes after midnight')
    ax.set_title(f'Timetable for {day}')
    plt.tight_layout()
    if out_path:
        plt.savefig(out_path)
        print('Saved plot to', out_path)
    else:
        plt.show()
    return fig
