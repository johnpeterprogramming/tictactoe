board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def print_board(board):
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

first = input("X or O? ")

if first == 'X':
    player = 'X'
    ai = 'O'
else:
    player = 'O'
    ai = 'X'

score_index = {
    'X' : 1,
    'O' : -1,
    'tie' : 0
}

def check_win(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != '':
                count += 1
               
        #horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
        #vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '': 
            return board[0][i]


    #diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != '':
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != '':
        return board[1][1]

    if count == 9:
        return 'tie'

    return None

def minimax(brd, depth, isMaximizing):
    eval = check_win(brd)
    if eval:
        return score_index[eval] * 1/depth

    if isMaximizing:
        best_score = -100
        for i in range(3):
            for j in range(3):
                if brd[i][j] == '':
                    if first == 'O':
                        brd[i][j] = ai
                    else:
                        brd[i][j] = player

                    score = minimax(brd, depth+1, False)
                    brd[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        min_score = 100
        for i in range(3):
            for j in range(3):
                if brd[i][j] == '':
                    if first == 'O':
                        brd[i][j] = player
                    else:
                        brd[i][j] = ai
                    score = minimax(brd, depth+1, True)
                    brd[i][j] = ''
                    min_score = min(score, min_score)
        return min_score

def bestMove():
    if first == "O":
        bestScore = -100
    else:
        minScore = 100

    for i in range(3):
        for j in range(3):
            if board[i][j] == '': #spot is available
                board[i][j] = ai
                if first == 'O':
                    score = minimax(board, 1, False)
                else:
                    score = minimax(board, 1, True)

                # print(f"score: {score}, row:{i}, col:{j}")
                board[i][j] = ''
                if first == "O":
                    if score > bestScore:
                        bestScore = score
                        move = (i, j)
                else:
                    if score < minScore:
                        minScore = score
                        move = (i, j)
    return move

def get_player_input():
    while True:
            
            move = int(input("> "))
            move -= 1

            row = move // 3
            column = move % 3

            if board[row][column] == '':
                board[row][column] = player
                return

            print("Can't make move there")

for _ in range(9):
    if first == 'O':
        ai_move = bestMove()
        board[ai_move[0]][ai_move[1]] = ai

        winner = check_win(board)
        if winner:
            break
        print_board(board)

        get_player_input()
        winner = check_win(board)
        if winner:
            break
    else:
        print_board(board)
        get_player_input()
        winner = check_win(board)
        if winner:
            break

        ai_move = bestMove()
        board[ai_move[0]][ai_move[1]] = ai

        winner = check_win(board)
        if winner:
            break

if winner != 'tie':
    print("-------------")
    print(f"Player {winner} won!")
    print("-------------")
else:
    print("--------")
    print("DRAW ")
    print("--------")

    print()

print_board(board)
