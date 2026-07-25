import subprocess
import os
def open_edge():
    try:
        subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
        return "Microsoft Edge Opened Successfully"
    except:
        try:
            subprocess.Popen([r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"])
            return "Microsoft Edge Opened Successfully"
        except Exception as e:
            return f"Error: {e}"
        
def open_chrome():
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    return "Google Chrome Opened Successfully"
def open_notepad():
    os.system("notepad")
    return "Notepad Opened Successfully"
def open_calculator():
    os.system("calc")
    return "Calculator Opened Successfully"
def open_cmd():
    os.startfile("cmd.exe")
    return "Command Prompt Opened Successfully"
def open_vscode():
    os.system("code")
    return "Visual Studio Code Opened Successfully"