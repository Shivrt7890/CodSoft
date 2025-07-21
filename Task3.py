import tkinter as tk
import random
from tkinter import messagebox

# Initialize scores
user_score = 0
computer_score = 0

# Game logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=f"You: {user_choice} | Computer: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

    # Ask if the user wants to play again
    play_more = messagebox.askyesno("Next Round", "Do you want to play another round?")
    if not play_more:
        window.quit()

# Set up window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("320x300")
window.configure(bg="lightblue")

# Title
tk.Label(window, text="Rock - Paper - Scissors", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)

# Buttons
tk.Button(window, text="Rock", width=12, command=lambda: play("Rock")).pack(pady=5)
tk.Button(window, text="Paper", width=12, command=lambda: play("Paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=12, command=lambda: play("Scissors")).pack(pady=5)

# Result label
result_label = tk.Label(window, text="Make your move!", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=15)

# Score label
score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="lightblue")
score_label.pack(pady=10)

# Run the GUI
window.mainloop()
