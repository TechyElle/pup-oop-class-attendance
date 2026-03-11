<div align="center">

# 📋 PUP OOP Class Attendance System
### *Select your section. Get your location. Time in with ease.*

![Python](https://img.shields.io/badge/Python-Backend-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-Data_Storage-217346?style=for-the-badge&logo=files&logoColor=white)
![GPS](https://img.shields.io/badge/GPS-Location_Verified-FF6F00?style=for-the-badge&logo=googlemaps&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge)

> A Python-based class attendance system for **PUP OOP** students.  
> Students time in using GPS location verification while teachers monitor records via an admin dashboard.

</div>

---

## 🌟 What It Does

| Feature | Description |
|--------|-------------|
| 📍 **GPS Verification** | Detects student location and validates they are within campus range |
| 🏫 **Section Selection** | Dropdown to select section, then loads matching student names |
| ⏱️ **Student Time-In** | Records student name, section, timestamp, and GPS accuracy |
| 🔐 **Admin Login** | Secure teacher/admin login to access the attendance dashboard |
| 📊 **Attendance Records** | View all time-in logs with name, section, date, time, and accuracy |

---

## 📁 Project Structure

```text
pup-oop-class-attendance/
|
|-- main.py                  # Entry point and main menu
|-- student_view.py          # Student time-in logic and flow
|-- admin_view.py            # Teacher/admin login and dashboard
|-- location_handler.py      # GPS acquisition and campus validation
|-- attendance_manager.py    # Record and display attendance logic
|-- file_handler.py          # Read/write CSV file
|-- attendance_data.csv      # Stored attendance records
`-- README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd pup-oop-class-attendance
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Project

```bash
python main.py
```

Main menu options:
- `1` — Student Time-In
- `2` — Teacher/Admin Login
- `3` — Exit

---

## 🖥️ How to Use

### Student Time-In
1. Select **"1. Student Time-In"** from the main menu
2. Choose your **Section** from the dropdown
3. Choose your **Name** from the loaded list
4. Wait for **GPS location** to be acquired (`Getting Location...` → `Location Obtained`)
5. Press **Time In** — location is validated and attendance is recorded

### Teacher / Admin Login
1. Select **"2. Teacher/Admin Login"** from the main menu
2. Enter your **username** and **password**
3. View the attendance table:

| Student Name | Section | Date | Time In | Accuracy (m) |
|---|---|---|---|---|
| juan_dela_cruz | BSIT-1A | 2026-03-11 | 08:45:00 | 50 |

---

## ✅ Implementation Notes

```text
✔ Section-based student loading   -> names populate only after section is selected
✔ GPS status updates              -> "Getting Location..." -> "Location Obtained (Accuracy: Xm)"
✔ Haversine distance formula      -> calculates meters between student and campus coords
✔ Campus boundary validation      -> rejects time-in if student exceeds 500m from campus
✔ Timestamped records             -> saves date and time at moment of time-in
✔ CSV persistence                 -> attendance data saved and reloaded across sessions
✔ Snake_case naming standard      -> applied to all variables, functions, and filenames
```

---

## 📐 Coding Standards

| Element | Convention | Example |
|---|---|---|
| Variables | snake_case | `selected_section` |
| Functions | snake_case | `record_time_in()` |
| Constants | UPPER_SNAKE_CASE | `MAX_DISTANCE_METERS` |
| Files | snake_case | `attendance_manager.py` |
| Classes | PascalCase | `AttendanceRecord` |

---

## 🧩 Tech Stack

- **Python 3.8+** — core application logic
- **CSV** — lightweight local data storage
- **Math (Haversine)** — GPS distance calculation
- **Datetime** — timestamp generation

---

<div align="center">

⚠️ *For educational purposes only. Created for the PUP Object-Oriented Programming course.*

</div>
