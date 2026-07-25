import subprocess

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