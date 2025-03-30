import pandas as pd
from db import users_collection, disaster_collection
from opencage.geocoder import OpenCageGeocode
from math import radians, sin, cos, sqrt, atan2
from send_emails import send_email

# ✅ Correct Data Extraction
users = list(users_collection.find({}, {"city": 1, "email": 1, "_id": 0}))  # Fetch city, email
disasters = list(disaster_collection.find({}, {"Region": 1, "Title": 1, "URL": 1, "Published At": 1, "_id": 0}))

# ✅ Convert to DataFrame
uc = pd.DataFrame(users)
dc = pd.DataFrame(disasters)

user_loc = uc['city'].tolist()
user_mail = uc['email'].tolist()
dis_loc = dc['Region'].tolist()
dis_til = dc['Title'].tolist()
dis_url = dc['URL'].tolist()
dis_pub = dc['Published At'].tolist()

# ✅ OpenCage API for Geocoding
OPENCAGE_API_KEY = "d417b701036946ddb48e34a35c389150"
geocoder = OpenCageGeocode(OPENCAGE_API_KEY)

def get_lat_lon(location):
    """Fetch latitude and longitude for a given location."""
    if not location or location.lower() == "unknown":
        return None, None  # Handle missing locations

    try:
        geo_data = geocoder.geocode(location)
        if geo_data:
            return geo_data[0]['geometry']['lat'], geo_data[0]['geometry']['lng']
    except Exception as e:
        print(f"Error fetching coordinates for {location}: {e}")
    
    return None, None  

def alert(x, y):
    """Send disaster alert email to user."""
    send_email(
        to_email=user_mail[y],
        subject=f"🚨 Disaster Alert in {user_loc[y]}",
        message=f"""
        Title: {dis_til[x]}
        URL: {dis_url[x]}
        Published At: {dis_pub[x]}
        """
    )

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate great-circle distance (in km) between two latitude-longitude points."""
    if None in (lat1, lon1, lat2, lon2):
        return float('inf')  # Return very large distance if any coordinate is missing

    R = 6371.0  # Earth's radius in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c  # Distance in km

def is_inside_danger_zone(disaster_lat, disaster_lon, user_lat, user_lon, radius_km):
    """Check if user is inside the disaster danger zone."""
    return haversine_distance(disaster_lat, disaster_lon, user_lat, user_lon) <= radius_km

# ✅ Get Latitude & Longitude for Users and Disasters
ull = [get_lat_lon(loc) for loc in user_loc]
dll = [get_lat_lon(loc) for loc in dis_loc]

# ✅ Check & Send Alerts
danger_radius_km = 100

for x, (dis_lat, dis_lon) in enumerate(dll):
    if dis_lat is None or dis_lon is None:
        continue  # Skip disasters with invalid coordinates

    for y, (user_lat, user_lon) in enumerate(ull):
        if user_lat is None or user_lon is None:
            continue  # Skip users with invalid coordinates

        if is_inside_danger_zone(dis_lat, dis_lon, user_lat, user_lon, danger_radius_km):
            alert(x, y)
