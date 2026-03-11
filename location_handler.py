# location_handler.py
# Description: Handles GPS simulation and campus location validation

import time

def get_gps_location():
    # SHOW status: acquiring GPS
    print("\n  📍 Getting Location...")
    print("  ⏳ Acquiring GPS location...")

    # SIMULATE a short GPS acquisition delay
    time.sleep(1.5)

    # SIMULATE obtained GPS coordinates and accuracy
    # In a real app, this would call a GPS/geolocation API
    simulated_latitude     = 14.5998
    simulated_longitude    = 120.9840
    simulated_accuracy     = 50

    # SHOW success status with accuracy
    print(f"  ✅ Location obtained (Accuracy: {simulated_accuracy}m)")
    return simulated_latitude, simulated_longitude, simulated_accuracy
