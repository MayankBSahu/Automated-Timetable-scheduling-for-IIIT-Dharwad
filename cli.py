# Simple CLI/demo to load sample dataset and run validation / print
import argparse, os
from timetable_automation import database, scheduler, visualizer, exporter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='sample_data/timetable_aug_dec_2025.json')
    args = parser.parse_args()
    data = database.load_dataset(args.data)
    s = scheduler.Scheduler(data['courses'], faculty=data['faculty'], rooms=data['rooms'], students=data['students'], rules=data.get('rules',{}))
    print('Validating...')
    conf = s.validate()
    if conf:
        print('Conflicts found:')
        for c in conf:
            print(' -', c)
    else:
        print('No conflicts found.')
    s.print_timetable_by_day()
    # export CSV
    exporter.export_sessions_csv(data['courses'], 'sample_data/sessions_export.csv')

if __name__ == '__main__':
    main()
