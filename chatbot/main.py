from bot import ChatBot

def main():
    bot = ChatBot()
    print("ChatBot: Hello! Type 'bye' to exit.")
    
    while True:
        try:
            user_input = input("You: ")
            if not user_input:
                continue
                
            response = bot.get_response(user_input)
            print(f"ChatBot: {response}")
            
            if user_input.lower().strip() == "bye":
                break
                
        except KeyboardInterrupt:
            print("\nChatBot: Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
