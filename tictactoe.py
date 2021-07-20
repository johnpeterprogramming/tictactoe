board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def print_board():
    count = 1
    for i in range(3):
        line = str()
        for j in range(3):
            if board[i][j] == '':
                line += str(count)
            else:
                line += str(board[i][j])
            if j < 2:
                line += ' | '

            count += 1

        print(line)
        if i < 2:
            print("---------")

players = ("X", "O")
player = 'X'
ai = 'O'

score_index = {
    player : 1,
    ai : -1,
    'tie' : 0
}

def check_win(board):
    winner = None
    draw = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                draw = False
                break

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

    if draw:
        return 'tie'

def minimax(board, depth, isMaximizing):
    eval = check_win(board)
    if eval:
        return score_index[eval]
    
    if isMaximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = ai
                    score = minimax(board, depth+1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        min_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = player
                    score = minimax(board, depth+1, True)
                    board[i][j] = ''
                    min_score = min(score, min_score)
        return min_score

for _ in range(9):
    print_board()
    while True:
        
        move = int(input("> "))
        move -= 1

        row = move // 3
        column = move % 3

        if board[row][column] == '':
            board[row][column] = player
            break

        print("Can't make move there")

    winner = check_win(board)
    if winner:
        break

    best_score = float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == '': #spot is available
                board[i][j] = ai
                score = minimax(board, 0, False)
                board[i][j] = ''
                if score < best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = ai

    winner = check_win(board)
    if winner:
        break

if winner != 'tie':
    print("-------------")
    print(f"Player {winner} won!")
    print("-------------")
else:
    print("-------------")
    print("DRAW ")
    print("-------------")

    print()
print_board()
