import json
import os

PROFILE_FILE = "database/profile.json"

def save_profile(profile):
    os.makedirs("database", exist_ok = True)
    with open(PROFILE_FILE, "w") as file:
        json.dump(profile, file, indent=4)
        
def load_profile():
    if not os.path.exists(PROFILE_FILE):
        return {}
    with open(PROFILE_FILE, "r") as file:
        return json.load(file)