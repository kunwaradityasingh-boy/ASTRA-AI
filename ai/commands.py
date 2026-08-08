from automation.apps import open_edge
from automation.browse import open_website, google_search
from automation.files import open_folder, open_file, create_folder
from automation.apps import(open_notepad, open_calculator, open_cmd, open_vscode, open_chrome, open_whatsapp)
import webbrowser
import subprocess
import os
print("*******COMMANDS.PY LOADED********")
def open_any_website(command):
    site = command.replace("open", "").strip().replace("", "")
    
    if "." not in site:
        site += ".com"
    webbrowser.open(f"https://{site}")
    return f"Opened {site}"

def execute_command(command):
    print("COMMAND RECEIVED =", repr(command))
    command = command.lower()
    
    if "open edge" in command:
        print(open_edge())
    elif "open website" in command:
        url = command.replace("open website", "").strip()
        print(open_website(url))
    elif "open folder" in command:
        path = command.replace("open folder", "").strip()
        print(open_folder(path))
    elif "open file" in command:
        path = command.replace("open file", "").strip()
        print(open_file(path))
    elif "create folder" in command:
        path = command.replace("create folder", "").strip()
        print(create_folder(path))
    elif "open notepad" in command:
        print(open_notepad())
    elif "open calculator" in command:
        print(open_calculator())
    elif "open cmd" in command:
        print(open_cmd())
    elif "open vscode" in command or "open vs code" in command:
        print(open_vscode())
    elif "open github" in command:
        print(open_website("github.com"))
    elif "open youtube" in command:
        print(open_website("youtube.com"))
    elif "open google" in command:
        print("OPEN GOOGLE BLOCK")
        print(open_website("google.com"))
        return
    elif "google" in command:
        print("OPEN GOOGLE BLOCK")
        query = command.replace("google", "",1).strip()
        
        if query:
            print(google_search(query))
        else:
            print(open_website("google.com"))
    elif "open chrome" in command:
        print(open_chrome())
    elif "open whatsapp" in command:
        print(open_whatsapp())
    elif command.startswith("open "):
        print(open_any_website(command))
    else:
        print("Command not found")