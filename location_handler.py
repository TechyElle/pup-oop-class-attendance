# location_handler.py
# Description: Handles GPS simulation and campus location validation

import time
import math

# Campus coordinates (PUP Manila)
CAMPUS_LATITUDE     = 14.5995
CAMPUS_LONGITUDE    = 120.9842
MAX_DISTANCE_METERS = 500

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

def calculate_distance(current_latitude, current_longitude):
    # USE the Haversine formula to calculate distance from campus
    earth_radius_meters = 6_371_000

    lat_diff = math.radians(current_latitude - CAMPUS_LATITUDE)
    lon_diff = math.radians(current_longitude - CAMPUS_LONGITUDE)

    a = (
        math.sin(lat_diff / 2) ** 2
        + math.cos(math.radians(CAMPUS_LATITUDE))
        * math.cos(math.radians(current_latitude))
        * math.sin(lon_diff / 2) ** 2
    )

    distance_meters = earth_radius_meters * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return distance_meters

def validate_location(current_latitude, current_longitude):
    # CALCULATE distance from campus coordinates
    distance_meters = calculate_distance(current_latitude, current_longitude)

    # IF within campus range, return True
    if distance_meters <= MAX_DISTANCE_METERS:
        return True

    # ELSE student is outside campus range
    return False
