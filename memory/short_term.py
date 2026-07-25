memory = []

def remember(test):
    memory.append(test)
    print(f"Remembered: {test}")
    
def recall():
    return memory