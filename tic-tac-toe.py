board=['-','-','-',
       '-','-','-',
       '-','-','-']

player="X"

winner=None
game_is_going=True

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_turn():
    position=int(input("Enter the position from 0 to 8:"))
    if board[position]=="-":
       board[position]=player
       swap_player()


def swap_player():
    global player
    if player=="X":
        player="O"
    elif player=="O":
        player="X"

def check_winner():
    global winner
    rowwinner=row()
    colwinner=col()
    diawinner=dia()
    check_draw()
    if rowwinner:
        winner=rowwinner
    elif colwinner:
        winner=colwinner
    elif diawinner:
        winner=diawinner


def row():
    global game_is_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_is_going=False

    if row1:
        return  board[2]
    elif row2:
        return board[4]
    elif row3:
        return board[6]

    return

def col():
    global game_is_going
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        game_is_going=False

    if col1:
        return  board[6]
    elif col2:
        return board[4]
    elif col3:
        return board[5]

    return

def dia():
    global game_is_going
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"


    if dia1 or dia2:
        game_is_going=False

    if dia1:
        return  board[0]
    elif dia2:
        return board[4]
    return
def check_draw():
    global game_is_going
    if "-" not in board:
        game_is_going=False
        return



def play_game():
    while game_is_going:
        global position
        display_board()

        player_turn()


        check_winner()

    if winner=="X":
       print("X is the winner")
    elif winner=="O":
         print("O is the winner")
    elif winner== None:
         print("draw match")
play_game()
