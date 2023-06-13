"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0
    num_empty = 0

    for row in board:
        for play in row:
            if play == X:
                num_x += 1
            elif play == O:
                num_o += 1
            else:
                num_empty += 1
    
    if num_empty == 9:
        return X
    elif num_o < num_x:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    next_player = player(board)
    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                position = (i, j)
                possible_actions.add(position)

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Raising exception if the location of the action is out of bound
    for i in action:
        if i > 2:
            raise ValueError
        elif board[action[0]][action[1]] != EMPTY:
            raise ValueError
    # Creating a deep copy of the board
    r_board = deepcopy(board) 
    # Finding the next player turn using the player function
    next_player = player(board)
    # Storing the next player input on the action location 
    r_board[action[0]][action[1]] = next_player
    # Returning the updated board
    return r_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking all the rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
        
    # checking all the columns
    for j in range(len(board)):
      col = ''
      for i in range(len(board)):
        col += str(board[i][j])
      if col == 'XXX':
        return X
      if col == 'OOO':
        return O
      
    # Checking diagonals
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
      
      # if winner not found return none
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if a player has won or if there are any actions left
    if winner(board) or not actions(board):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_player(board)
            return move
        else:
            value, move = min_player(board)
            return move


def min_player(board):
    if terminal(board):
        return utility(board), None

    optimal_move = None
    neg_value = float('inf')
    for action in actions(board):
        aux, act = max_player(result(board, action))
        if aux < neg_value:
            neg_value = aux
            optimal_move = action
            if neg_value == -1:
                return neg_value, optimal_move

    return neg_value, optimal_move


def max_player(board):
    if terminal(board):
        return utility(board), None

    optimal_move = None
    pos_value = float('-inf')
    for action in actions(board):
        aux, act = min_player(result(board, action))
        if aux > pos_value:
            pos_value = aux
            optimal_move = action
            if pos_value == 1:
                return pos_value, optimal_move

    return pos_value, optimal_move
