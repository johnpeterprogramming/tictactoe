board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board():
    for i in range(3):
        print(f"{board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("---------")

players = ("X", "O")
current_index = 0

def check_win():
    winner = 0
    for i in range(3):
        #horizontal
        if board[i][0] == board[i][1] == board[i][2]:
            winner = board[i][0]
            return winner
        #vertical
        if board[0][i] == board[1][i] == board[2][i]: 
            winner = board[0][i]
            return winner

    #diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[1][1]
        return winner
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[1][1]
        return winner

move = 1

while True:
    print_board()
    print(f"Player {players[current_index]}'s move")
    can_move = False
    while not can_move:
        move_row = int(input("What Row? "))
        move_column = int(input("What Column? "))
        if board[move_row-1][move_column-1] == ' ':
            board[move_row-1][move_column-1] = players[current_index]
            current_index = (current_index + 1) % 2
            break
        print("Can't make move there")
    if check_win() == 'X':
        print("-------------")
        print("Player X won!")
        print("-------------")
        break
    elif check_win() == 'O':
        print("-------------")
        print("Player O won!")
        print("-------------")
        break
    move += 1
    if move == 10:
        print("-------------")
        print("DRAW, YOU BOTH SUCK")
        print("-------------")
        break

    print()
print_board()
