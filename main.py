# main.py
# Description: Entry point for PUP OOP Class Attendance System

from student_view import run_student_time_in
from admin_view import run_admin_login

def show_main_menu():
    # DISPLAY the main menu header and options
    print("\n" + "=" * 45)
    print("     PUP OOP Class Attendance System")
    print("=" * 45)
    print("  [1] Student Time-In")
    print("  [2] Teacher / Admin Login")
    print("  [3] Exit")
    print("=" * 45)
