import random
import tkinter as tk
from tkinter import font

player_score = 0
computer_score = 0

options = ("Rock", 'Paper', "Scissors")

beats = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}

def get_computer_choice():
    return random.choice(options)

def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text=f"You selected: {player_input}")
    computer_choice_label.config(text=f"Computer selected: {computer_input}")

    if player_input == computer_input:
        result = "It's a tie!"
    elif beats[player_input] == computer_input:
        player_score += 1
        result = "You won!"
    else:
        computer_score += 1
        result = "Computer won!"

    winner_label.config(text=result)
    player_score_label.config(text=f"Your score: {player_score}")
    computer_score_label.config(text=f"Computer score: {computer_score}")



game_window = tk.Tk()
game_window.title("Rock Paper Scissors Game")
game_window.geometry("700x300")

app_font = font.Font(size=12)
title_font = font.Font(size=20)
winner_font = font.Font(size=13)

game_title = tk.Label(game_window, text="Rock Paper Scissors", font=title_font)
game_title.pack(pady=(12, 0))

winner_label = tk.Label(
    game_window,
    text="Choose Rock, Paper, or Scissors to start.",
    font=winner_font,
    fg="green",
)
winner_label.pack(pady=8)

input_frame = tk.Frame(game_window)
input_frame.pack()

player_options = tk.Label(input_frame, text="Your options", font=app_font)
player_options.grid(row=0, column=0, columnspan=3, pady=8)

rock_btn = tk.Button(
    input_frame, text="Rock", width=15, bg="pink",
    command = lambda: player_choice('Rock'),
)
rock_btn.grid(row=1, column=0, padx=8, pady=5)

paper_btn = tk.Button(
    input_frame, text="Paper", width=15, bg="silver",
    command = lambda: player_choice('Paper'),
)
paper_btn.grid(row=1, column=1, padx=8, pady=5)

scissors_btn = tk.Button(
    input_frame, text="Scissors", width=15, bg="light blue",
    command = lambda: player_choice('Scissors'),
)
scissors_btn.grid(row=1, column=2, padx=8, pady=5)

player_choice_label = tk.Label(input_frame, text="You selected: ---", font=app_font)
player_choice_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=8, pady=5)

computer_choice_label = tk.Label(
    input_frame, text="Computer selected: ---", font = app_font,
)
computer_choice_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=8, pady=5)

player_score_label = tk.Label(input_frame, text="Your score: 0", font=app_font)
player_score_label.grid(row=2, column=2, sticky="w", padx=8, pady=5)

computer_score_label = tk.Label(input_frame, text="Computer score: 0", font=app_font)
computer_score_label.grid(row=3, column=2, sticky="w", padx=8, pady=5)

game_window.mainloop()
