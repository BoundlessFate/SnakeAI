import random
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
def moveAi(board, hamiltonian, boardSize, skipCount):
    # Check if you can jump ahead in the cycle
    newHamiltonian = hamiltonian.copy()
    currentPos = (0,0)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                currentPos = (i,j)   
    currentHamil = hamiltonian[currentPos[0]][currentPos[1]]
    if skipCount <= 0:
        # Modify the hamiltonian so the current snake head is at pos 1 is at cycle. Shift everything else
        for i in range(len(newHamiltonian)):
            for j in range(len(newHamiltonian[i])):
                if newHamiltonian[i][j] >= currentHamil:
                    newHamiltonian[i][j] -= (currentHamil - 1)
                else:
                    newHamiltonian[i][j] += ((boardSize ** 2) - currentHamil) + 1
        modifiedHeadSpot = 1
        boardMax = np.max(board)
        tailPosList = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] >= 1:
                    tailPosList.append(newHamiltonian[i][j])
        tailPos = min(tailPosList)
        # Down,up,left,right checks to see how much would be skipped if moved there
        spotSkips = []
        if currentPos[0] + 1 < boardSize:
            spotSkips.append((newHamiltonian[currentPos[0] + 1][currentPos[1]] - 1, 's'))
        if currentPos[0] - 1 >= 0:
            spotSkips.append((newHamiltonian[currentPos[0] - 1][currentPos[1]] - 1, 'w'))
        if currentPos[1] + 1 < boardSize:
            spotSkips.append((newHamiltonian[currentPos[0]][currentPos[1] + 1] - 1, 'd'))
        if currentPos[1] - 1 >= 0:
            spotSkips.append((newHamiltonian[currentPos[0]][currentPos[1] - 1] - 1, 'a'))
        # Pop the highest index (would be going backwards)
        maxSkipTuple = (0,'w')
        maxSkipSpot = 0
        for i in spotSkips:
            if i[0] > maxSkipSpot:
                maxSkipTuple = i
                maxSkipSpot = i[0]
        spotSkips.pop(spotSkips.index(maxSkipTuple))
        spotSkips.sort(reverse = True)
        blockedSpots = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] >= 1 and not board[i][j] == boardMax:
                    blockedSpots.append(newHamiltonian[i][j] - 1)
        for i in range(len(spotSkips) - 1, -1, -1):
            if spotSkips[i][0] in blockedSpots:
                spotSkips.pop(i)
        # Find the maximum distance that can be skipped
        maxPossibleSkip = (boardSize ** 2) - tailPos
        # Find distance to apple through normal hamiltonian cycle
        applePos = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    applePos = newHamiltonian[i][j] - 1
                    break
            if not applePos == 0:
                break
        # loop through possible moves, prioritizing the maximum possible jump towards the apple at each spot
        for skip in spotSkips:
            if skip[0] <= applePos:
                return (skip[1], len(tailPosList))
    # If you can't jump ahead in the cycle, move normally through the hamiltonian

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
        return ('w', skipCount - 1)
    elif currentPos[0] + 1 == nextHamilPos[0]:
        return ('s', skipCount - 1)
    elif currentPos[1] - 1 == nextHamilPos[1]:
        return ('a', skipCount - 1)
    else:
        return ('d', skipCount - 1)

valid = False
while not valid:
    boardSize = int(input('Enter Board Size: ').strip())
    if boardSize % 2 == 0:
        valid = True
    else:
        print('Invalid Board Size! Enter In A Even Number.')
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
skipCount = 0
while ongoing:
    display_board(board)
    print()
    move = moveAi(board,hamiltonian, boardSize, skipCount)
    print('Move: {}'.format(move[0]))
    skipCount = move[1]
    data = move_snake(board, move[0])
    board = data[0]
    ongoing = data[1]
    length = np.max(board)
    print('Length: {}'.format(length))
    print('Moves before it can skip: {}'.format(skipCount))
    moveCount += 1
    if length == boardSize ** 2:
        ongoing = False
        display_board(board)
        print('Game Won. Took {} Moves.'.format(moveCount))
