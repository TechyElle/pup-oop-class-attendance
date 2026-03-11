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


def main():
    # LOOP continuously until the user chooses to exit
    while True:
        # DISPLAY main menu
        show_main_menu()
        user_choice = input("  Enter choice: ").strip()

        # IF choice is Student Time-In
        if user_choice == "1":
            run_student_time_in()

        # IF choice is Teacher/Admin Login
        elif user_choice == "2":
            run_admin_login()

        # IF choice is Exit → break the loop
        elif user_choice == "3":
            print("\n  Goodbye! See you next class.\n")
            break

        # ELSE → invalid input
        else:
            print("\n  [!] Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
