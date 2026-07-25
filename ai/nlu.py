def detect_intent(command):
    command = command.lower().strip()
    
    intents = {
        "OPEN_CHROME": [
            "open chrome",
            "chrome kholo",
            "chrome open karo",
            "google chrome kholo",
            "browser kholo",
            "chrome chalao",
            "chrome khol do",
            "browser khol do",
            "google khol do"
        ],
        
        "OPEN_NOTEPAD": [
            "open notepad",
            "notepad kholo",
            "notepad chalao",
            "notepad khol do"
        ],
        
        "OPEN_VSCODE": [
            "open vs code",
            "vs code kholo",
            "virtual studio code kholo",
            "vscode kholo",
            "vs code khol do"
        ]
    }
    
    for intent, phrases in intents.items():
        for phrase in phrases:
            if phrase in command:
                return intent
            
    return "UNKNOWN"