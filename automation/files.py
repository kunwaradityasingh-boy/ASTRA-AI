import os
import subprocess

def open_folder(path):
    try:
        os.startfile(path)
        return f"opened folder: {path}"
    except Exception as e:
        return f"Error: {e}"
    
def open_file(path):
    try:
        os.startfile(path)
        return f"opened file: {path}"
    except Exception as e:
        return f"Error: {e}"
    
def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        return f"folder created: {path}"
    except Exception as e:
        return f"Error: {e}"
