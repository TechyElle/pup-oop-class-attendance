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



def show_admin_dashboard():
    print("\n  ✅ Login successful. Welcome, Admin!")

    # LOOP the admin dashboard until logout is chosen
    while True:
        print("\n" + "=" * 45)
        print("         Teacher / Admin Dashboard")
        print("=" * 45)
        print("  [1] View All Attendance Records")
        print("  [2] View Records by Section")
        print("  [3] Logout")
        print("=" * 45)

        admin_choice = input("  Enter choice: ").strip()

        # IF choice is View All Records
        if admin_choice == "1":
            display_attendance_records()

        # IF choice is View by Section → ask for section name first
        elif admin_choice == "2":
            selected_section = input("  Enter section name (e.g. BSIT-1A): ").strip()
            display_attendance_by_section(selected_section)

        # IF choice is Logout → exit the dashboard loop
        elif admin_choice == "3":
            print("\n  Logged out successfully.")
            break

        # ELSE invalid choice
        else:
            print("\n  [!] Invalid choice. Please enter 1, 2, or 3.")

