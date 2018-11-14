from constraint import *
import numpy as np

# Setup Problem
problem = Problem()

# Setup board
N = 7
board = np.array([[0 for j in range(N)] for i in range(N)])

# Setup Black Boxes, number indicates the black boxes needed 5 is for empty black box
# 6 is for 0 with black box, 7 for boxes with 1

# Board 1
board[0][2] = 6
board[0][5] = 5

board[1][0] = 5
board[1][4] = 5

board[2][1] = 2
board[2][6] = 6

board[3][3] = 7

board[4][0] = 7
board[4][5] = 5

board[5][2] = 7
board[5][6] = 3

board[6][1] = 6
board[6][4] = 5

# Board 2
# board[0][3] = 2
#
# board[1][2] = 5
# board[1][4] = 7
#
# board[2][1] = 5
# board[2][5] = 6
#
# board[3][0] = 6
# board[3][3] = 3
# board[3][6] = 5
#
# board[4][1] = 7
# board[4][5] = 2
#
# board[5][2] = 5
# board[5][4] = 5
#
# board[6][3] = 7

def findSmallestRow(boardRow, j):
    # imaginary box
    smallest = -1
    for i in range(N):
        if boardRow[i] != 0 and j > i:
            smallest = i

    return smallest


def findMaximumRow(boardRow, j):
    largest = N
    for i in reversed(range(N)):
        if boardRow[i] != 0 and j < i:
            largest = i

    return largest


def addSmallestRowConstraint(board, i, j):
    # First travel rows and add them in a listö
    smallestBlackBoxRow = findSmallestRow(board[i], j)
    maximumBlackBoxRow = findMaximumRow(board[i], j)
    availableBulb = []
    # If its not in the list add
    for columnIndex in range(smallestBlackBoxRow + 1, maximumBlackBoxRow):
        if "x%i%s" % (i, columnIndex) not in availableBulb:
            availableBulb.append("x%i%s" % (i, columnIndex))

    # Check the transpose and run the same algorithm on it
    transposeBoard = board.transpose()
    smallestBlackBoxRow = findSmallestRow(transposeBoard[j], i)
    maximumBlackBoxRow = findMaximumRow(transposeBoard[j], i)

    for columnIndex in range(smallestBlackBoxRow + 1, maximumBlackBoxRow):
        if "x%i%s" % (columnIndex, j) not in availableBulb:
            availableBulb.append("x%i%s" % (columnIndex, j))

    # Add constraint
    problem.addConstraint(MinSumConstraint(1), availableBulb)


def addEachBoxAConstraint(board):
    for i in range(N):
        for j in range(N):
            # Light bulbs are initially all the boxes with 0 value
            if board[i][j] == 0:
                # Traverse and find spots to limit
                addSmallestRowConstraint(board, i, j)


def checkLeft(board, position):
    # check column
    if position[1] > 0:
        if board[position[0]][position[1] - 1] == 0:
            # Empty box
            return True
        else:
            # Black box
            return False
    # If its out of index
    else:
        return False


def checkTop(board, position):
    # check row
    if position[0] > 0:
        if board[position[0] - 1][position[1]] == 0:
            # Empty box
            return True
        else:
            # Black box
            return False
    # If its out of index
    else:
        return False


def checkRight(board, position):
    # check column N is board size
    if position[1] + 1 < N:
        if board[position[0]][position[1] + 1] == 0:
            # Empty box
            return True
        else:
            # Black box
            return False
    # If its out of index
    else:
        return False


def checkBottom(board, position):
    # check row N is board size
    if position[0] + 1 < N:
        if board[position[0] + 1][position[1]] == 0:
            # Empty box
            return True
        else:
            # Black box
            return False
    # If its out of index
    else:
        return False


def addBlockContraint(board):
    # Each row block can contain maximum 1 bulb
    for i in range(N):
        availableBulb = []
        for j in range(len(board[i])):
            if board[i][j] == 0:
                availableBulb.append("x%i%s" % (i, j))
            else:
                if availableBulb != []:
                    problem.addConstraint(MaxSumConstraint(1), availableBulb)
                availableBulb = []
        if availableBulb != []:
            problem.addConstraint(MaxSumConstraint(1), availableBulb)

    # Each column block can contain maximum 1 bulb
    boardT = board.transpose()
    for i in range(N):
        availableBulb = []
        for j in range(len(boardT[i])):
            if boardT[i][j] == 0:
                availableBulb.append("x%i%s" % (j, i))
            else:
                if availableBulb != [] and len(availableBulb) != 1:
                    problem.addConstraint(MaxSumConstraint(1), availableBulb)
                availableBulb = []
        if availableBulb != []:
            problem.addConstraint(MaxSumConstraint(1), availableBulb)

# Initiliaze light bulbs
for i in range(N):
    for j in range(N):
        # Light bulbs are initially all the boxes with 0 value
        if board[i][j] == 0:
            problem.addVariable("x%i%s" % (i, j), [0, 1])

# Set contraints for light bulbs around black boxes
for i in range(N):
    for j in range(N):
        # Search for black boxes that is filled with a number
        if board[i][j] != 0 and board[i][j] != 5:
            availableBulb = []
            # one of these conditions must hold
            if checkLeft(board, [i, j]):
                availableBulb.append("x%i%s" % (i, j - 1))
            if checkTop(board, [i, j]):
                availableBulb.append("x%i%s" % (i - 1, j))
            if checkRight(board, [i, j]):
                availableBulb.append("x%i%s" % (i, j + 1))
            if checkBottom(board, [i, j]):
                availableBulb.append("x%i%s" % (i + 1, j))
            # Add the sum constraint

            if board[i][j] == 6:
                problem.addConstraint(ExactSumConstraint(0), availableBulb)
            elif board[i][j] == 7:
                problem.addConstraint(ExactSumConstraint(1), availableBulb)
            else:
                problem.addConstraint(ExactSumConstraint(board[i][j]), availableBulb)

# Add row and Column constraints
addEachBoxAConstraint(board)
addBlockContraint(board)
solution = problem.getSolutions()
print(solution)
