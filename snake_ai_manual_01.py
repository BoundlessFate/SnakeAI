import random
def create_apple(board):
    possibleList = []
    for i in range(len(board)):
        for j in range(len(board[i])):
                if board[i][j] == 0:
                    possibleList.append((i,j))
    if len(possibleList) >= 1:
        appleSpot = possibleList[random.randint(0, len(possibleList) - 1)]
        board[appleSpot[0]][appleSpot[1]] = -1
    return board
def display_board(board):
    for i in range(len(board)):
        string = ''
        for j in range(len(board[i])):
            currentVal = board[i][j]
            if currentVal == 0:
                string += '· '
            elif currentVal == -1:
                string += 'A '
            elif currentVal == 1:
                string += 'S '
            else:
                string += '* '
        print(string)
def move_snake(board, move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Increment The Snake Pos
            if not board[i][j] <= 0:
                board[i][j] += 1
    maxPos = (0,0)
    max = 0
    boardMaximum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > boardMaximum:
                boardMaximum = board[i][j]
   # Get current position of the snake head
    currentPos = (0,0)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:
                currentPos = (i,j)
    applePos = (0,0)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == -1:
                applePos = (i,j)
    if move == 'w':
        # Check if out of board range
        if not (currentPos[0] - 1 < 0):
            # Check if snake hit itself
            if not (board[currentPos[0] - 1][currentPos[1]] >= 1) or (board[currentPos[0] - 1][currentPos[1]] == boardMaximum):
                print('test')
                ongoing = True
                if (currentPos[0] - 1, currentPos[1]) == applePos:
                    create_apple(board)
                else:
                    # Delete the last part of the snake
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if board[i][j] > max:
                                maxPos = (i,j)
                                max = board[i][j]
                    board[maxPos[0]][maxPos[1]] = 0
                board[currentPos[0] - 1][currentPos[1]] = 1
            else:
                ongoing = False
        else:
            ongoing = False
    elif move == 'a':
        if not (currentPos[1] - 1 < 0):
            if not (board[currentPos[0]][currentPos[1] - 1] >= 1) or (board[currentPos[0]][currentPos[1] - 1] == boardMaximum):
                print('test')
                ongoing = True
                if (currentPos[0], currentPos[1] - 1) == applePos:
                    create_apple(board)
                else:
                    # Delete the last part of the snake
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if board[i][j] > max:
                                maxPos = (i,j)
                                max = board[i][j]
                    board[maxPos[0]][maxPos[1]] = 0
                board[currentPos[0]][currentPos[1] - 1] = 1
            else:
                ongoing = False
        else:
            ongoing = False
    elif move == 's':
        # Check if out of board range
        if not (currentPos[0] + 1 >= len(board)):
            # Check if snake hit itself
            if not (board[currentPos[0] + 1][currentPos[1]] >= 1) or (board[currentPos[0] + 1][currentPos[1]] == boardMaximum):
                print('test')
                ongoing = True
                if (currentPos[0] + 1,currentPos[1]) == applePos:
                    create_apple(board)
                else:
                    # Delete the last part of the snake
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if board[i][j] > max:
                                maxPos = (i,j)
                                max = board[i][j]
                    board[maxPos[0]][maxPos[1]] = 0
                board[currentPos[0] + 1][currentPos[1]] = 1
            else:
                ongoing = False
        else:
            ongoing = False
    elif move == 'd':
        if not (currentPos[1] + 1 >= len(board[0])):
            if not (board[currentPos[0]][currentPos[1] + 1] >= 1) or (board[currentPos[0]][currentPos[1] + 1] == boardMaximum):
                print('test')
                ongoing = True
                if (currentPos[0], currentPos[1] + 1) == applePos:
                    create_apple(board)
                else:
                    # Delete the last part of the snake
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if board[i][j] > max:
                                maxPos = (i,j)
                                max = board[i][j]
                    board[maxPos[0]][maxPos[1]] = 0
                board[currentPos[0]][currentPos[1] + 1] = 1
            else:
                ongoing = False
        else:
            ongoing = False
    return (board, ongoing)

board_length = int(input('Enter Board Length: ').strip())
print(str(board_length))
board_width = int(input('Enter Board Width: ').strip())
print(str(board_width))
board = []
snake_length = 1
# Create The Base Board
for i in range(board_length):
    board.append([])
    for j in range(board_width):
        board[i].append(0)
snake_starting_length = random.randint(0, board_length - 1)
snake_starting_width = random.randint(0, board_width - 1)
board[snake_starting_length][snake_starting_width] = 1
board = create_apple(board)
ongoing = True
while ongoing:
    display_board(board)
    move = input('Enter A Move (wasd): ').strip()
    data = move_snake(board, move)
    board = data[0]
    ongoing = data[1]
