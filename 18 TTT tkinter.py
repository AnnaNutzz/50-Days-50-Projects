import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="#333")  # BG color

board = [" " for _ in range(9)] 
player = "X" 
computer = "O" 
gameover = False

# Colors
BUTTON_COLOR = "#35CAA3"
BUTTON_ACTIVE_COLOR = "#2B967C"
BUTTON_FONT = ("Arial", 24, "bold")
TEXT_COLOR_X = "#CA355C"  # X color
TEXT_COLOR_O = "#5935CA"  # O color

def check_winner(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:
            return True
    return False

def is_full(board):
    return " " not in board

# Heuristic function
def heuristic(board):
    score = 0
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        line = [board[i] for i in condition]
        if line.count(computer) == 2 and line.count(" ") == 1:
            score += 10 # Favor computer two-in-a-row
        elif line.count(player) == 2 and line.count(" ") == 1:
            score -= 10 # Discourage player two-in-a-row
    return score

# Minimax with heuristic
def minimax(board, depth, is_maximizing):
    if check_winner(board, computer):
        return 100
    if check_winner(board, player):
        return -100
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = computer
                score = minimax(board, depth + 1, False) + heuristic(board)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                score = minimax(board, depth + 1, True) + heuristic(board)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI's move
def ai_move():
    best_score = -float("inf")
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = computer
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    update_board(move, computer)

def update_board(position, mark):
    global gameover
    board[position] = mark
    buttons[position].config(
        text=mark, 
        fg=TEXT_COLOR_X if mark == player else TEXT_COLOR_O
    )
    if check_winner(board, mark):
        gameover = True
        messagebox.showinfo("Game Over", f"{mark} wins!")
        reset_game()
    elif is_full(board):
        gameover = True
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()

def player_move(position):
    global gameover
    if board[position] == " " and not gameover:
        update_board(position, player)
        if not gameover:
            ai_move()

def reset_game():
    global board, gameover
    board = [" " for _ in range(9)]
    gameover = False
    for button in buttons:
        button.config(text=" ", fg="black", bg=BUTTON_COLOR)

# Create the GUI board
buttons = []
for i in range(9):
    button = tk.Button(
        root, text=" ", font=BUTTON_FONT, width=5, height=2,
        bg=BUTTON_COLOR, activebackground=BUTTON_ACTIVE_COLOR,
        command=lambda i=i: player_move(i)
    )
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

# Start the game
root.mainloop()
