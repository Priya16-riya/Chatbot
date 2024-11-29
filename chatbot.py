import nltk
from nltk.chat.util import Chat, reflections

# Define conversation patterns
pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there!"]),
    (r"what is your name?", ["I'm a chatbot created by you. What's your name?"]),
    (r"how are you?", ["I'm just a bunch of code, but I'm doing fine! How about you?"]),

    (r"exit", ["Goodbye! Have a great day!"]),
    (r"(.*)", ["Sorry, I didn't understand that. Could you please rephrase?"]),
    
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Chatbot: Hi! Type 'quit' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")

 

    

