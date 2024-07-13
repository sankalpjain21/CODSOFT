#------------------------Rock Paper Scissors Game-----------------------------

import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def update_result(user_choice):
    global user_score, computer_score
    
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    user_choice_label.config(text=f"You chose: {user_choice}", fg="blue")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}", fg="red")
    
    if result == "tie":
        result_label.config(text="It's a tie!", fg="orange")
    elif result == "user":
        result_label.config(text="You win!", fg="green")
        user_score += 1
    else:
        result_label.config(text="You lose!", fg="red")
        computer_score += 1
    
    score_text.set(f"Scores - You: {user_score}, Computer: {computer_score}")
    
    ask_play_again()

def ask_play_again():
    play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if not play_again:
        root.destroy()

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")
    score_text.set("Scores - You: 0, Computer: 0")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

user_score = 0
computer_score = 0

score_text = tk.StringVar()
score_text.set("Scores - You: 0, Computer: 0")

title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Arial', 16, 'bold'), bg="#f0f0f0")
title_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=15, command=lambda: update_result("rock"), bg="#add8e6")
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(button_frame, text="Paper", width=15, command=lambda: update_result("paper"), bg="#90ee90")
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=15, command=lambda: update_result("scissors"), bg="#ffb6c1")
scissors_button.grid(row=0, column=2, padx=5, pady=5)

user_choice_label = tk.Label(root, text="", font=('Arial', 12, 'bold'), bg="#f0f0f0")
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="", font=('Arial', 12, 'bold'), bg="#f0f0f0")
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'), bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, textvariable=score_text, font=('Arial', 12, 'bold'), bg="#f0f0f0")
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, bg="#f08080")
reset_button.pack(pady=20)

root.mainloop()
