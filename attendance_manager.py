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

def display_attendance_records():
    # LOAD all records from the CSV file
    attendance_records = load_attendance_from_csv()

    # IF no records exist, notify and return early
    if not attendance_records:
        print("\n  [!] No attendance records found.")
        return

    # DISPLAY table header
    print("\n" + "=" * 70)
    print(f"  {'Student Name':<22} {'Section':<10} {'Date':<13} {'Time In':<10} {'Accuracy'}")
    print("=" * 70)

    # FOR each record, print its details in a formatted row
    for record in attendance_records:
        print(
            f"  {record['student_name']:<22}"
            f" {record['section']:<10}"
            f" {record['date']:<13}"
            f" {record['time_in']:<10}"
            f" {record['location_accuracy']}"
        )

    print("=" * 70)
