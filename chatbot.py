from tkinter import *
from tkinter.scrolledtext import ScrolledText

class ChatBot:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")
        
        self.chat_history = ScrolledText(master, wrap=WORD)
        self.chat_history.pack(expand=True, fill=BOTH)

        self.user_input = Entry(master, width=50)
        self.user_input.pack(side=LEFT, padx=10, pady=10, expand=True, fill=X)

        send_button = Button(master, text="Send", command=self.send)
        send_button.pack(side=RIGHT, padx=10, pady=10)

    def send(self):
        user_input_text = self.user_input.get()
        self.display_user_message(user_input_text)
        self.generate_response(user_input_text)
        self.user_input.delete(0, END)

    def display_user_message(self, message):
        self.chat_history.insert(END, "You: " + message + "\n")
        self.chat_history.see(END)

    def display_bot_message(self, message):
        self.chat_history.insert(END, "Bot: " + message + "\n")
        self.chat_history.see(END)

    def generate_response(self, user_input):
        user_input = user_input.lower()
        if any(word in user_input for word in ["hello", "hi"]):
            self.display_bot_message("Hi there!")
        elif "how are you" in user_input:
            self.display_bot_message("I'm just a bot, but I'm functioning well. How can I assist you?")
        elif "your name" in user_input:
            self.display_bot_message("I'm a chatbot! You can call me Chatbot.")
        elif "thank you" in user_input:
            self.display_bot_message("You're welcome!")
        elif "bye" in user_input:
            self.display_bot_message("Goodbye! Have a great day!")
        else:
            self.display_bot_message("I didn't quite get that. Can you please rephrase?")

def main():
    root = Tk()
    chatbot_app = ChatBot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
