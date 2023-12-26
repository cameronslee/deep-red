# Deep Red - Simple Chess Engine

import chess

move_number = 0
MAX_VAL = 42069


# State - Handle board state and legal moves
class State(object):
  def __init__(self, board=None):
    if board is None:
      self.board = chess.Board()
    else:
      self.board = board

  def legal_moves(self):
    return list(self.board.legal_moves)

# Evaluation function - estimate "goodness" of a position in a game tree
# essentially the entire engine 
class Evaluator(object):
  # Shannon values
  values = {chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 200}

  def __init__(self):
    pass

  def eval(self, move):
    total = 0.0

    pm = s.board.piece_map()

    # calculate piece score
    for i in pm:
      val = self.values[pm[i].piece_type]
      if pm[i].color == chess.WHITE:
        total += val
      elif pm[i].color == chess.BLACK:
        total -= val

    # TODO Calculate Doubled Pawns
    # TODO Calculate Blocked Pawns
    # TODO Calculate Isolated Pawns
    
    # calculate mobility
    temp = s.board.turn

    # Calculate mobility of white
    s.board.turn = chess.WHITE
    total += 0.1 * len(s.legal_moves())

    s.board.turn = chess.BLACK
    total -= 0.1 * len(s.legal_moves())

    s.board.turn = temp

    return total

### ====== Game State and Evaluator ======= ###
s = State()
v = Evaluator()
### ======================================= ###


# TODO can simplify into negamax 
# White: Maximizing Player
# Black: Minimizing Player
# node is a move
def minimax(s, depth, maximizingPlayer):
  if depth == 0 or s.board.is_game_over():
    return v.eval(s) # position node
  curr_turn = s.board.turn

  if curr_turn == chess.WHITE:
    value = -MAX_VAL
    '''
    for child in s:
      value = max(value, minimax(child, depth-1, chess.BLACK))
    '''

  elif curr_turn == chess.BLACK:
    value = MAX_VAL
    '''
    for child in s:
      value = min(value, minimax(child, depth-1, chess.WHITE))
    '''

 
  temp = []
  for m in s.board.legal_moves:
    s.board.push(m)
    # evaluate current position
    temp.append((v.eval(m), m))
    s.board.pop()
 

  print("Moves available: ", temp)

  return temp

  #return value

### ====== Move Functionality ====== ###

# moves are in UCI notation
def player_move(move):
  try:
    print("Moving ", move)
    s.board.push_uci(str(move))
  except:
    print("error: invalid player movement")
  

def computer_move():
  # build game tree
  moves = minimax(s, 3, s.board.turn)
  print(moves[0])
  
  
if __name__ == "__main__":
  running = True
  print("Welcome to Deep Red")
  print(s.board)
  print(s.board.piece_map())

  while(running):
    if (move_number != 0):
      print(s.board)

    move = input("Enter a move: ")
    print(move)
    player_move(move)
    move_number += 1
    computer_move()
