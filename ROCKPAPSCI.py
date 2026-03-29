import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock Paper Scissor=")
comp_choice = random.choice(item_list)

print(f"User choice {user_choice}, Computer choice is {comp_choice}")

if user_choice == comp_choice :
    print("TIE!!!")

elif user_choice == "Rock" and comp_choice == "Paper":
    print("YOU LOSE!!!")

elif user_choice == "Rock" and comp_choice == "Scissor":
    print("YOU WIN!!!")
elif user_choice == "Paper" and comp_choice == "Rock":
    print("YOU WIN!!!")

elif user_choice == "Paper" and comp_choice == "Scissor":
    print("YOU LOSE!!!")
elif user_choice == "Scissor" and comp_choice == "Rock":
    print("YOU LOSE!!!")
elif user_choice == "Scissor" and comp_choice == "Paper":
    print("YOU WIN!!!")


""" print(f"...") is using an f-string (formatted string) in Python.

🔹 What is f?

The f before the quotes tells Python:
👉 “Hey, this string will contain variables or expressions inside it.”

🔹 Basic Example
name = "Kajol"
print(f"Hello {name}")"""
