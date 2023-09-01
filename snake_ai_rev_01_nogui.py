import random
import time
import numpy as np
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
def createHamiltonian(boardSize):
    # Create Board Of All Zeroes
    board = []
    for i in range(boardSize):
        board.append([])
        for j in range(boardSize):
            board[i].append(0)
    # Top Left = 1
    board[0][0] = 1
    count = 2
    # Go up and down the rows excluding the first row and increment
    # Looping through columns
    for i in range(len(board)):
        # if going down
        if i % 2 == 0:
            for j in range(1, len(board)):
                board[j][i] = count
                count += 1
        # if going up
        else:
            for j in range(len(board) -1, 0, -1):
                board[j][i] = count
                count += 1
    # Increment the rest of the top row excluding the top left
    for i in range(len(board[0]) - 1, 0, -1):
        board[0][i] = count
        count += 1
    return board
def moveAi(board, hamiltonian):
    currentPos = (0,0)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                currentPos = (i,j)
    currentHamil = hamiltonian[currentPos[0]][currentPos[1]]
    if currentHamil == len(board) ** 2:
        nextHamil = 1
    else:
        nextHamil = currentHamil + 1
    nextHamilPos = (0,0)
    for i in range(len(hamiltonian)):
        for j in range(len(hamiltonian)):
            if hamiltonian[i][j] == nextHamil:
                nextHamilPos = (i,j)
    if currentPos[0] - 1 == nextHamilPos[0]:
        return 'w'
    elif currentPos[0] + 1 == nextHamilPos[0]:
        return 's'
    elif currentPos[1] - 1 == nextHamilPos[1]:
        return 'a'
    else:
        return 'd'
valid = False
while not valid:
    boardSize = int(input('Enter Board Size: ').strip())
    if boardSize % 2 == 0:
        valid = True
    else:
        print('Invalid Board Size! Enter In A Even Number.')
timeStart = time.time()
board = []
snake_length = 1
# Create The Base Board
for i in range(boardSize):
    board.append([])
    for j in range(boardSize):
        board[i].append(0)
# Add The Snakes Starting Position
snake_starting_length = random.randint(0, boardSize - 1)
snake_starting_width = random.randint(0, boardSize - 1)
board[snake_starting_length][snake_starting_width] = 1
# Generate Original Apple
board = create_apple(board)
# Create Initial Hamiltonian
hamiltonian = createHamiltonian(boardSize)
# Loop To Play Game
ongoing = True
moveCount = 0
while ongoing:
    move = moveAi(board,hamiltonian)
    data = move_snake(board, move)
    board = data[0]
    ongoing = data[1]
    length = np.max(board)
    moveCount += 1
    if length == boardSize ** 2:
        ongoing = False
        print('Game Won. Took {} Moves.'.format(moveCount))
timeEnd = time.time()
timeTotal = timeEnd - timeStart
print('Time To Complete: {}'.format(timeTotal))
print('Time Per Thousand Moves: {}'.format(timeTotal/(moveCount/1000)))
