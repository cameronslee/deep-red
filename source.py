# Deep Red - Simple Chess Engine

import chess

move_number = 0
MAX_VAL = 42069

# Evaluation function - estimate "goodness" of a position in a game tree
# essentially the entire engine 
class Evaluator(object):
  # shannon values
  values = {chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 4000}

  def __init__(self):
    pass

  def evaluate():
    pass

# State - Handle board state and legal moves
class State(object):
  def __init__(self, Board=None):
    if board is None:
      self.board = chess.Board()
    else:
      self.board = board

  def legal_moves(self):
    return list(self.board.legal_moves)

### ====== Game State and Evaluator ======= ###
s = State()
v = Evaluator()


# TODO can simplify into negamax 
# White: Maximizing Player
# Black: Minimizing Player
def minimax(state, eval, node, depth, maximizingPlayer):
  if depth == 0 or state.board.is_game_over():
    return node # position node
  curr_turn = state.board.turn

  if curr_turn == chess.WHITE:
    value = -MAX_VAL
    for child in node:
      value = max(value, minimax(child, depth-1, chess.BLACK))
    return value
  else:
    value = MAX_VAL
    for child in node:
      value = max(value, minimax(child, depth-1, chess.WHITE))
    return value
### ====== Move Functionality ====== ###

def player_move():
  pass

def computer_move():
  pass
  
if __name__ == "__main__":

  board = chess.Board()
  running = True

  print("Welcome to Deep Red")
  print(board)

  while(running):
    if (move_number != 0):
      print(board)

    move = input("Enter a move: ")
    print(move)
    move_number += 1





