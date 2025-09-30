import json, os
from .models import Course, Faculty, Room, Student
from typing import List

def load_dataset(path: str):
    with open(path,'r',encoding='utf-8') as f:
        j = json.load(f)
    courses = [Course.from_dict(c) for c in j.get('courses',[])]
    faculty = [Faculty.from_dict(f) for f in j.get('faculty',[])]
    rooms = [Room.from_dict(r) for r in j.get('rooms',[])]
    students = [Student.from_dict(s) for s in j.get('students',[])]
    return {
        'meta': j.get('meta',{}),
        'rules': j.get('rules',{}),
        'courses': courses,
        'faculty': faculty,
        'rooms': rooms,
        'students': students
    }

def save_dataset(path: str, data: dict):
    # data expected to be dict with lists of dataclass instances
    out = {}
    for k in ('meta','rules'):
        if k in data: out[k]=data[k]
    out['courses'] = [c.to_dict() for c in data.get('courses',[])]
    out['faculty'] = [vars(f) for f in data.get('faculty',[])]
    out['rooms'] = [vars(r) for r in data.get('rooms',[])]
    out['students'] = [vars(s) for s in data.get('students',[])]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,'w',encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
