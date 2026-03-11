# student_view.py
# Description: Handles the student time-in flow

from location_handler import get_gps_location, validate_location
from attendance_manager import record_time_in

# Student roster grouped by section
SECTION_STUDENT_LIST = {
    "BSCPE 1-1": [
        "Juan Dela Cruz",
        "Maria Santos",
        "Pedro Reyes",
        "Anna Lopez",
        "Carlos Garcia",
    ],
    "BSCPE 1-2": [
        "Jose Rizal",
        "Andres Bonifacio",
        "Emilio Aguinaldo",
        "Apolinario Mabini",
        "Melchora Aquino",
    ],
    "BSCPE 1-3": [
        "Miguel Ramos",
        "Sofia Cruz",
        "Liza Hernandez",
        "Marco Villanueva",
        "Nina Castillo",
    ],
}
      
def select_section():
    section_list = list(SECTION_STUDENT_LIST.keys())

    # DISPLAY available sections
    print("\n  --- Select Section ---")
    for index, section_name in enumerate(section_list, start=1):
        print(f"  [{index}] {section_name}")

    # INPUT user's section choice and validate
    while True:
        section_choice = input("  Enter section number: ").strip()

        # IF valid choice, return the selected section name
        if section_choice.isdigit() and 1 <= int(section_choice) <= len(section_list):
            selected_section = section_list[int(section_choice) - 1]
            return selected_section

        # ELSE show error and prompt again
        print("  [!] Invalid choice. Please try again.")


def select_student_name(selected_section):
    # LOAD the student list for the selected section
    student_list = SECTION_STUDENT_LIST[selected_section]

    # DISPLAY student names
    print(f"\n  --- Select Your Name ({selected_section}) ---")
    for index, student_name in enumerate(student_list, start=1):
        print(f"  [{index}] {student_name}")

    # INPUT name choice and validate
    while True:
        name_choice = input("  Enter your number: ").strip()

        # IF valid choice, return the selected student name
        if name_choice.isdigit() and 1 <= int(name_choice) <= len(student_list):
            selected_student_name = student_list[int(name_choice) - 1]
            return selected_student_name

        # ELSE show error and prompt again
        print("  [!] Invalid choice. Please try again.")
