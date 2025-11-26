class ChatBot:
    def __init__(self):
        self.rules = {
            "hello": "Hello there! How can I help you?",
            "hi": "Hi! What's on your mind?",
            "how are you": "I'm just a bot, but I'm doing great! How about you?",
            "bye": "Goodbye! Have a nice day!",
            "help": "I can respond to greetings and simple questions. Try saying 'hello'!"
        }

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check for exact matches first
        if user_input in self.rules:
            return self.rules[user_input]
        
        # Check for partial matches or keywords
        for key in self.rules:
            if key in user_input:
                return self.rules[key]
                
        return "I'm sorry, I didn't understand that. Type 'help' to see what I can do."
