
import random
import re

# Define intents and responses
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Greetings! How can I help you?"]
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you later"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },
    "hours": {
        "patterns": ["working hours", "office hours", "when are you open"],
        "responses": ["We are open from 9 AM to 5 PM, Monday to Friday."]
    },
    "help": {
        "patterns": ["can you help me", "i need assistance", "help"],
        "responses": ["Of course! How can I assist you today?"]
    }
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if re.search(pattern, user_input):
                return random.choice(data["responses"])
    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop
print("Chatbot: Hello! Type 'bye' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
