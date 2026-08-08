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
        ],
        
        "OPEN_GITHUB": [
            "open github",
            "github kholo",
            "github chalao",
            "github khol do",
            "github open karo"
        ],
        
        "OPEN_YOUTUBE": [
            "open youtube",
            "youtube kholo",
            "youtube chalao",
            "youtube khol do",
            "youtube open karo"
        ],
        
        "OPEN_GOOGLE": [
            "open google",
            "google kholo",
            "google chalao",
            "google khol do",
            "google open karo"
        ],
        
        "OPEN_WHATSAPP": [
            "open whatsapp",
            "whatsapp kholo",
            "whatsapp chalao",
            "whatsapp khol do",
            "whatsapp open karo"
        ],
        
        "EXIT": [
            "exit",
            "stop",
            "quit",
            "close",
            "goodbye",
            "bye",
            "stop listening",
            "band ho jao",
            "band karo",
            "exit karo"
        ]
    }
    
    for intent, phrases in intents.items():
        for phrase in phrases:
            if phrase in command:
                return intent
            
    return "UNKNOWN"