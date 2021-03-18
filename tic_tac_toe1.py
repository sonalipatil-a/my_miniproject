'''create board
two players
flip(swap) players
check who is winner
row(3)
columns(3)
diagonals(3)
drawn'''

# create board
board=["-","-","-",
       "-","-","-",
       "-","-","-",]
current_player="X"
winner =None
gameisgoing=True


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn():
    position=int(input("Choose random position from 0 to 8 :"))
    board[position]=current_player

def swap_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"

def check_who_is_winner():
    global winner
    rowwinner=check_row()
    colwinner=check_column()
    diawinner=check_diagonal()
    check_tie()
    if rowwinner:
        winner=rowwinner
    elif colwinner:
        winner=colwinner
    elif diawinner:
        winner=diawinner

def check_row():
    global gameisgoing
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        gameisgoing=False
    if row1:
        return board[0]
    elif row2:
        return board[4]
    elif row3:
        return board[6]
def check_column():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        gameisgoing=False
    if col1:
        return board[0]
    elif col2:
        return board[4]
    elif col3:
        return board[8]
def check_diagonal():
    global gameisgoing
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"
    if dia1 or dia2 :
        gameisgoing = False
    if dia1:
        return board[0]
    elif dia2:
        return board[4]

def check_tie():
    global gameisgoing
    if "-" not in board:
        gameisgoing=False
        print("Match is Tried")
def play_game():
    while gameisgoing:
        display_board()
        handle_turn()
        swap_player()
        check_who_is_winner()
        if winner=="X":
            print("X is winner")
        elif winner=="O":
            print("O is winner")



play_game()