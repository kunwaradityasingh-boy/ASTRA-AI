conversation = []

def add_message(role, content):
    conversation.append({
        "role":role,
        "parts":[{"text":content}]
    })
    
    if len(conversation) > 10:
        conversation.pop(0)
        
def get_context():
    return conversation