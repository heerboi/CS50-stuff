"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # Initial state is empty board
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nox = 0
    noo = 0
    # Check for the total X's and O's in the board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                nox += 1
            elif board[i][j] == O:
                noo += 1
    # If the game is over
    if (nox == 5 and noo == 4) or (nox == 4 and noo == 5):
        return None
    # If the number of X's is greater than O's
    elif nox > noo:
        return O
    # If the number of O's is greater than X's
    elif noo > nox:
        return X
    # If it is the first turn
    elif noo == 0 and nox == 0:
        return X
    # If the number of O's are equal to X's, return X
    # as the first turn will always be X
    elif nox == noo:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # All actions that can be performed
    act = set()
    # Check for empty spaces on the board, and add them to the set
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == None:
                act.add((i, j))
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Initiate the (x,y) to two separate variables
    x, y = action
    # Get the player whose turn it is
    turn = player(board)
    # If the given action (x, y) is not empty, raise exception
    if board[x][y] != None:
        raise RuntimeError("Invalid action.")
    # make a deepcopy of the board so as to preserve the current board
    boardcpy = copy.deepcopy(board)
    boardcpy[x][y] = turn
    return boardcpy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # If there is a 3-pair in any of the diagonals
    if check_diag(board) != None:
        return check_diag(board)
    # If there is a 3-pair in any of the rows or columns
    elif check_rowcol(board) != None:
        return check_rowcol(board)
    # If there are no empty spaces or if the game in progress
    elif sum(None in lis for lis in board) == 0 or player(board) != None:
        return None

def check_diag(board):
    # board[i][i] will return values such as board[0][0], [1][1] and [2][2]
    # If the set of these values is zero and the element is not None, it means
    # that one of the two players have a 3-pair
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != None:
        return board[0][0]
    # board[i][len(board) - 1 - i] will return values such as board[0][2], [1][1], [2][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1 and board[0][len(board) - 1] != None:
        return board[0][len(board) - 1]
    return None

def check_rowcol(board):
    # Check each row
    for row in board:
        # If any row has three same elements which are not None,
        # a 3-pair is found
        if len(set(row)) == 1 and row[0] != None:
            return row[0]
    # Check each column
    for c in range(len(board)):
        # Here, [0][c], [1][c], [2][c] will return the column values for column number c
        # If these values are similar and not none, a 3-pair is found
        if len(set([board[0][c], board[1][c], board[2][c]])) == 1 and board[0][c] != None:
            return board[0][c]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there are no more possible actions or if the winner is not none, game is over
    if actions(board) == set() or winner(board) != None:
        return True
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # if x wins, 1
    if winner(board) == X:
        return 1
    # if o wins, -1
    elif winner(board) == O:
        return -1
    # else, 0
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_move = None
    if terminal(board):
        return None
    # if the current player is X, maximizing player
    if player(board) == X:
        # Set a var m to -ve infinity as the maximizing player will always have values over -ve infinity
        m = -math.inf
        # for all the actions, the opposite player will try to minimize the score
        for a in actions(board):
            # calculate the minimizing score for the opponent for a given action
            n = minimum(result(board, a))
            # out of these minimized scores by opponent, we have to choose the highest
            # if the value is higher than previous, set it as m, and best_move as the action
            if n > m:
                m = n
                best_move = a
    # if the current player is O, minimizing player
    if player(board) == O:
        # Set it +ve infinity as minimizing player will always have values less than +ve infinity
        m = math.inf
        # for all actions possible, the opposite player will try to maximize the score
        for a in actions(board):
            # Calculate the maximizing score for the opponent for a given action
            n = maximum(result(board, a))
            # as we want the lowest score because we are the minimizing player,
            # check if the prev. value is higher than this, if so, set it as m and best_move as action
            if n < m:
                m = n
                best_move = a
    # return the best_move
    return best_move


def maximum(board):
    # If it is the terminal board, return utility (-1, 1, 0)
    if terminal(board):
        return utility(board)
    # set v as -infinity as maximum will always return a value greater than -infinity
    v = -math.inf
    # for all actions possible ahead, we have to look for the actions having highest score
    for a in actions(board):
        # check if v is greater or if the minimized score by the opponent for the next resultant board is greater
        v = max(v, minimum(result(board, a)))
    return v

def minimum(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    # for all actions, we have to look for the actions with lowest possible score
    for a in actions(board):
        # calculate the lowest value out of v and the maximized score for the resultant board
        v = min(v, maximum(result(board, a)))
    # return it
    return v