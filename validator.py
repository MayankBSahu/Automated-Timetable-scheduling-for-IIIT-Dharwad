from typing import List, Tuple
from .models import Course, Session, Student
import collections

def time_overlap(a_start, a_end, b_start, b_end):
    return not (a_end <= b_start or b_end <= a_start)

def parse_time_range(time_str):
    # "09:00-10:30" -> (start_min, end_min)
    try:
        s,e = time_str.split('-')
        h1,m1 = map(int, s.split(':'))
        h2,m2 = map(int, e.split(':'))
        return h1*60 + m1, h2*60 + m2
    except Exception:
        return None, None

def faculty_conflicts(courses: List[Course], min_gap_minutes: int = 180):
    # returns list of conflict descriptions
    conflicts = []
    by_fac = collections.defaultdict(list)
    for c in courses:
        for s in c.sessions:
            by_fac[c.instructorID].append((c.courseCode, s))
    for fid, sessions in by_fac.items():
        # check pairwise overlaps or gap violations same day
        for i in range(len(sessions)):
            for j in range(i+1, len(sessions)):
                ci, si = sessions[i]
                cj, sj = sessions[j]
                if si.day != sj.day:
                    continue
                a_start,a_end = parse_time_range(si.time)
                b_start,b_end = parse_time_range(sj.time)
                if a_start is None or b_start is None:
                    continue
                if time_overlap(a_start,a_end,b_start,b_end):
                    conflicts.append(f"Faculty {fid} overlap on {si.day}: {ci}@{si.time} vs {cj}@{sj.time}")
                else:
                    # check min gap between end and start
                    gap = abs(a_start - b_end) if a_start > b_end else abs(b_start - a_end)
                    if gap < min_gap_minutes:
                        conflicts.append(f"Faculty {fid} gap too small on {si.day}: {ci}@{si.time} vs {cj}@{sj.time} (gap {gap} min)")
    return conflicts

def student_conflicts(courses: List[Course], students: List[Student]):
    # Build mapping course->sessions per day/time, then for each student check overlaps
    conflicts = []
    course_map = {c.courseCode: c for c in courses}
    for st in students:
        st_sessions = []
        for code in st.registered_courses:
            c = course_map.get(code)
            if not c: continue
            for s in c.sessions:
                st_sessions.append((code, s))
        # check pairwise overlap
        for i in range(len(st_sessions)):
            for j in range(i+1, len(st_sessions)):
                ci, si = st_sessions[i]
                cj, sj = st_sessions[j]
                if si.day != sj.day: continue
                a_start,a_end = parse_time_range(si.time)
                b_start,b_end = parse_time_range(sj.time)
                if a_start is None or b_start is None: continue
                if time_overlap(a_start,a_end,b_start,b_end):
                    conflicts.append(f"Student {st.studentID} conflict on {si.day}: {ci}@{si.time} vs {cj}@{sj.time}")
    return conflicts
