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

def save_attendance_to_csv(attendance_records):
    # OPEN file in write mode, overwriting existing content
    with open(ATTENDANCE_FILE, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELD_NAMES)

        # WRITE the header row
        writer.writeheader()

        # FOR each record, write it as a CSV row
        for record in attendance_records:
            writer.writerow(record)
