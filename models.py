from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional
import datetime

@dataclass
class Session:
    day: str
    slot: str
    time: str  # "HH:MM-HH:MM"
    courseCode: str
    room: str
    type: str  # Lecture/Tutorial/Lab/Minor

    @staticmethod
    def from_dict(d):
        return Session(
            day=d.get('day'),
            slot=d.get('slot'),
            time=d.get('time'),
            courseCode=d.get('courseCode') or d.get('courseCode', d.get('course')),
            room=d.get('room') or d.get('roomID') or d.get('room_id',''),
            type=d.get('type','Lecture')
        )

    def to_dict(self):
        return asdict(self)

    def start_end_minutes(self):
        # returns (start_min, end_min) minutes from 00:00
        try:
            start, end = self.time.split('-')
            h1,m1 = map(int, start.split(':'))
            h2,m2 = map(int, end.split(':'))
            return h1*60+m1, h2*60+m2
        except Exception:
            return None

@dataclass
class Course:
    courseCode: str
    courseName: str
    LTPSC: str
    instructorID: str
    semester: int
    sessions: List[Session] = field(default_factory=list)
    category: str = "Core"

    @staticmethod
    def from_dict(d):
        sessions = [Session.from_dict(s) for s in d.get('sessions',[])]
        return Course(
            courseCode=d.get('courseCode'),
            courseName=d.get('courseName'),
            LTPSC=d.get('LTPSC',''),
            instructorID=d.get('instructorID') or d.get('instructor',''),
            semester=d.get('semester',0),
            sessions=sessions,
            category=d.get('category','Core')
        )

    def to_dict(self):
        d = asdict(self)
        d['sessions'] = [s.to_dict() for s in self.sessions]
        return d

@dataclass
class Faculty:
    facultyID: str
    name: str
    courses: List[str] = field(default_factory=list)
    preferred_slots: List[str] = field(default_factory=list)

    @staticmethod
    def from_dict(d):
        return Faculty(
            facultyID=d.get('facultyID') or d.get('id',''),
            name=d.get('name',''),
            courses=d.get('courses',[]),
            preferred_slots=d.get('preferred_slots', d.get('preferredSlots', []))
        )

@dataclass
class Room:
    roomID: str
    capacity: int = 0
    isLab: bool = False

    @staticmethod
    def from_dict(d):
        return Room(
            roomID=d.get('roomID') or d.get('room_id',''),
            capacity=d.get('capacity',0),
            isLab=d.get('isLab', False)
        )

@dataclass
class Student:
    studentID: str
    name: str
    batch: str
    registered_courses: List[str] = field(default_factory=list)

    @staticmethod
    def from_dict(d):
        return Student(
            studentID=d.get('studentID',''),
            name=d.get('name',''),
            batch=d.get('batch',''),
            registered_courses=d.get('registered_courses', d.get('registeredCourses', []))
        )
