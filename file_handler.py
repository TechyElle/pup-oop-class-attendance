# file_handler.py
# Description: Handles reading and writing attendance data to CSV

import csv
import os

ATTENDANCE_FILE = "attendance_data.csv"
CSV_FIELD_NAMES = ["student_name", "section", "date", "time_in", "location_accuracy"]

def load_attendance_from_csv():
    # IF the file does not exist yet, return an empty list
    if not os.path.exists(ATTENDANCE_FILE):
        return []

    # OPEN file and read all rows as dictionaries
    with open(ATTENDANCE_FILE, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        attendance_records = [row for row in reader]

    return attendance_records
