# admin_view.py
# Description: Handles Teacher/Admin login and attendance dashboard

from attendance_manager import display_attendance_records, display_attendance_by_section

# Admin credentials (in a real app, store securely in a database)
VALID_ADMIN_USERNAME = "admin"
VALID_ADMIN_PASSWORD = "pup2024"

MAX_LOGIN_ATTEMPTS = 3

def verify_admin_login(entered_username, entered_password):
    # IF credentials match the stored admin credentials, return True
    if entered_username == VALID_ADMIN_USERNAME and entered_password == VALID_ADMIN_PASSWORD:
        return True

    # ELSE credentials are invalid
    return False
