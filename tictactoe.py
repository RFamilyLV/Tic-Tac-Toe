# This program makes a Tic-Tac-Toe game.

# ----- Global Variables ----- #
game_still_going = True
winner = None
player = "X"
num_plays = 0

# Sets up the game board.
board = ["1", "2", "3", 
         "4", "5", "6", 
         "7", "8", "9"]

# Defines how to show the game board.
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Defines where the player wants there "X" or "O".
def player_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position 1-9: ")
    valid = False
    # Makes the game dummy proof.
    # It does this by making it so you can only input a number 1-9.
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("That is not a position 1-9")
            position = input("Choose a position 1-9: ")
        position = int(position) - 1
        if board[position] not in ["X", "O"]:
            valid = True
        else:
            print("Invalid input: You can not go there")
            print("Try again")
    board[position] = player
    display_board()

# Defines checking rows.
def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] and board[0] != "1"
    row_2 = board[3] == board[4] == board[5] and board[3] != "4"
    row_3 = board[6] == board[7] == board[8] and board[6] != "7"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

# Defines checking columns.
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] and board[0] != "1"
    column_2 = board[1] == board[4] == board[7] and board[1] != "2"
    column_3 = board[2] == board[5] == board[8] and board[2] != "3"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

# Defines checking diagonals.
def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] and board[0] != "1"
    diagonal_2 = board[6] == board[4] == board[2]

# Defines checking if someone won.
def check_if_win():
    global winner
    row_winner = check_rows()
    columns_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

# Defines checking if it was a tie.
def check_if_tie():
    global game_still_going
    global num_plays
    if ("1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" not in board) and num_plays == 9:
        game_still_going = False
    return

# Defines checking if the game is going.
def check_if_game_over():
    check_if_win()
    check_if_tie()

# Defines flipping between players.
def flip_player():
    global player
    global num_plays
    if player == "X":
        player = "O"
        num_plays = num_plays + 1
    elif player == "O":
        player = "X"
        num_plays = num_plays + 1
    return player

# Defines how to play the game.
def play_game():
    display_board()
    while game_still_going:
        player_turn(player)
        check_if_game_over()
        flip_player()
    # Game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# Plays the game
play_game()
