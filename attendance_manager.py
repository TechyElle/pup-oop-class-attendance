# attendance_manager.py
# Description: Handles recording and displaying attendance records

from datetime import datetime
from file_handler import save_attendance_to_csv, load_attendance_from_csv

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"

def record_time_in(student_name, selected_section, location_accuracy):
    # LOAD all existing records from file
    attendance_records = load_attendance_from_csv()

    # CREATE a new attendance record with current timestamp
    new_record = {
        "student_name"      : student_name,
        "section"           : selected_section,
        "date"              : datetime.now().strftime(DATE_FORMAT),
        "time_in"           : datetime.now().strftime(TIME_FORMAT),
        "location_accuracy" : f"{location_accuracy}m",
    }

    # APPEND the new record to the existing list
    attendance_records.append(new_record)

    # SAVE the updated list back to the CSV file
    save_attendance_to_csv(attendance_records)

    # SHOW success message
    print(f"\n  ✅ Time In recorded for {student_name} at {new_record['time_in']}")
