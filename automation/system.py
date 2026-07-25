from memory.short_term import recall, remember
from memory.long_term import save_memory, load_memory
from memory.profile import save_profile, load_profile

class System:
    def __init__(self):
        self.memory = load_memory()
        self.profile = load_profile()
        
    def remember(self, text):
        remember(text)
        self.memory.append(text)
        save_memory(self.memory)
        
    def recall(self):
        return recall()
    
    def save_profile(self, profile):
        save_profile(profile)
        self.profile = profile
        
    def get_profile(self):
        return self.profile        