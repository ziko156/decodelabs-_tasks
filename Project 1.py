name =  ""
def main():
    get_name()
    print("Hello " + name + ", How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "goodbye"]:
            print("Goodbye " + name + "! Have a great day!")
            break
        process_input(user_input)
def process_input(user_input):
    if user_input.lower() in ["how are you?", "how are you doing?"]:
            print("I'm doing well, thank you for asking! How can I assist you today?")
    elif user_input.lower() in ["what's your name?", "who are you?"]:
            print("My name is ChatBot, I'm here to assist you with any questions or tasks you may have.")
    elif user_input.lower() in ["what's the weather like?", "what's the weather?"]:
            print("I'm sorry, I don't have access to real-time weather information. However, you can check the weather on a website or app like Weather.com or AccuWeather.")
    elif user_input.lower() in ["what's the time?", "what time is it?"]:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("The current time is: " + current_time)
    else:
        print("I'm sorry, I don't understand. Can you please rephrase that?")

def get_name():
    global name
    print("Before we begin, what is your name? ")
    while True:
        name_input = input("You: ")
        if name_input.isalpha():
            name = name_input[0].upper() + name_input[1:].lower()
            break
        else:
            print("Only letters are allowed, no spaces. Please enter your name again.")
if __name__ == "__main__":    main()