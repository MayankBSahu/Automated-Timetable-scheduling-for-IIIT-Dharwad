from typing import List
from .models import Course, Session
from . import validator

class Scheduler:
    def __init__(self, courses: List[Course], faculty=None, rooms=None, students=None, rules=None):
        self.courses = courses
        self.faculty = faculty or []
        self.rooms = rooms or []
        self.students = students or []
        self.rules = rules or {}

    def validate(self):
        conflicts = []
        min_gap = self.rules.get('min_gap_between_same_faculty_lectures_minutes', 180)
        conflicts += validator.faculty_conflicts(self.courses, min_gap_minutes=min_gap)
        conflicts += validator.student_conflicts(self.courses, self.students)
        return conflicts

    def print_timetable_by_day(self):
        days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
        day_map = {d: [] for d in days}
        for c in self.courses:
            for s in c.sessions:
                day_map.setdefault(s.day, []).append((s, c.courseCode, c.courseName))
        # sort by start time
        for d in days:
            sessions = day_map.get(d, [])
            def start_min(item):
                s=item[0].time.split('-')[0]
                h,m=map(int,s.split(':'))
                return h*60+m
            sessions.sort(key=start_min)
            if sessions:
                print(f"\n{d}:")
                for s,code,name in sessions:
                    print(f"  {s.time} {s.slot} {code} {name} in {s.room} ({s.type})")

    def simple_resolve_room_conflicts(self):
        # naive method: if two sessions occupy same room/time, flag them. (no automatic moves yet)
        room_map = {}
        conflicts = []
        for c in self.courses:
            for s in c.sessions:
                key = (s.day, s.time, s.room)
                if key in room_map:
                    conflicts.append(f"Room conflict: {s.room} on {s.day} {s.time} between {room_map[key]} and {c.courseCode}")
                else:
                    room_map[key] = c.courseCode
        return conflicts
