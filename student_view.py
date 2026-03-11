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
