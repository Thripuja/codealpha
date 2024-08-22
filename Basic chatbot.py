def get_response(user_input):

    user_input = user_input.lower()

    # Define basic responses
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a simple chatbot created by OpenAI.",
        "bye": "Goodbye! Have a great day!",
        "default": "Sorry, I don't understand that."
    }
    return responses.get(user_input, responses["default"])

def chat():

    print("Chatbot: Hello! Type 'bye' to end the conversation.")

    while True:

        user_input = input("You: ")


        response = get_response(user_input)


        print(f"Chatbot: {response}")


        if user_input.lower() == "bye":
            break


# Run the chatbot
if __name__ == "__main__":
    chat()
