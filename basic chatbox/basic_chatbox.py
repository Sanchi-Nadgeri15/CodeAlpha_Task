def responsive():
    print("🤖 Chatbot: Hello! I'm your friendly assistant. Type 'bye' to exit.")

    greetings = ["hello", "hi", "hey", "hola", "namaste"]
    feeling_questions = ["how are you", "how are you doing", "how r u", "how's it going"]

    while True:
        user_input = input("👤 You: ").strip().lower()

        if user_input in greetings:
            print("🤖 Chatbot: Hey there! How can I help you today?")
        elif user_input in feeling_questions:
            print("🤖 Chatbot: I'm doing great, thanks for asking! What about you?")
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm just a simple chatbot built to assist you!")
        elif "help" in user_input:
            print("🤖 Chatbot: Sure! Ask me anything or just say hi.")
        elif "bye" in user_input or "exit" in user_input:
            print("🤖 Chatbot: Goodbye! Have a wonderful day! 👋")
            break
        else:
            print("🤖 Chatbot: I'm not sure I understand. Try asking something else.")

responsive()
