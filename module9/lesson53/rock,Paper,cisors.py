import tkinter as tk
import random

# List of choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
player_score = 0
computer_score = 0

# Function to determine winner
def play(player_choice):
    global player_score, computer_score
    
    computer_choice = random.choice(choices)
    
    result_text.set(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        outcome.set("It's a Tie!")
        
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        player_score += 1
        outcome.set("You Win!")
        
    else:
        computer_score += 1
        outcome.set("Computer Wins!")
    
    score_label.set(f"Player: {player_score}  Computer: {computer_score}")

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

# Variables for dynamic text
result_text = tk.StringVar()
outcome = tk.StringVar()
score_label = tk.StringVar()

# Title Label
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18)).pack(pady=10)

# Buttons Frame
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Result Labels
tk.Label(root, textvariable=result_text, font=("Arial", 12)).pack(pady=10)
tk.Label(root, textvariable=outcome, font=("Arial", 14)).pack(pady=5)
tk.Label(root, textvariable=score_label, font=("Arial", 12)).pack(pady=10)

root.mainloop()