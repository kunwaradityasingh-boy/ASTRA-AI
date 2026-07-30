from ai.assistant import Assistant

class AstraEngine:
    def __init__(self):
        print("ASTRA Engine Initialized")
        self.assistant = Assistant()
        
    def run(self):
        print("[ENGINE] Starting Assistant...")
        self.assistant.start()