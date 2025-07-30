# Statements

# Note : "else if" in JavaScript is "elif" in python.

# Example 1 : 
# user_input: str = "bye"

# if user_input == "Hellooooo":
#     print("Bot: Hello")
# elif user_input == "How are you?":
#     print("Bot: I'm doing good, what about you?")
# elif user_input == "bye":
#     print("Bot: bye bye!! Have a good day!!")
# else: 
#     print("Bot: Sorry I did not understand that!")

# Example 2 : 
while True:
    user_input: str = input("You: ")

    if user_input == "Hello":
        print("Bot: Hello")
    elif user_input == "How are you?":
        print("Bot: I'm doing good, what about you?")
    elif user_input == "bye":
        print("Bot: bye bye!! Have a good day!!")
    else: 
        print("Bot: Sorry I did not understand that!")