import json
import os

MEMORY_FILE = "database/memory.json"

def save_memory(data):
    os.makedirs("database", exist_ok=True)
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
def load_memory():
     if not os.path.exists(MEMORY_FILE):
         return []
     with open(MEMORY_FILE, "r") as file:
         return json.load(file)