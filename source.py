# Deep Red - Simple Chess Engine
import chess
import random

from flask import Flask, Response, request
app = Flask(__name__)

move_number = 0
MAX_VAL = 42069
MAX_DEPTH = 3

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
def minimax(s, depth, as_list=False):
  res = []
  if depth >= MAX_DEPTH or s.board.is_game_over():
    return v.eval(s) # position node

  curr_turn = s.board.turn

  if curr_turn == chess.WHITE:
    value = -MAX_VAL
  elif curr_turn == chess.BLACK:
    value = MAX_VAL
 
  # collect moves that can be made in current position
  temp = []
  for x in s.board.legal_moves:
    s.board.push(x)
    temp.append((v.eval(x), x))
    s.board.pop()
 
  for m in [t[1] for t in temp]:
    s.board.push(m)
    print(s.board)
    temp_val = minimax(s, depth+1)
    s.board.pop()

    res.append((v.eval(m), m))
    if s.board.turn == chess.WHITE:
      for child in temp:
        value = max(value, temp_val)
    else:
      for child in temp:
        value = min(value, temp_val)
  
  if as_list:
    return res, value
  return value 

### ====== Move Functionality ====== ###

def player_move(move):
  try:
    print("Player Moving ", move)
    s.board.push_san(move)
  except:
    print("error: invalid player movement")
  

def computer_move():
  # build game tree
  moves, value = minimax(s, 0, as_list=True)
  #print(moves)
  i = random.randint(0,len(moves))
  move = moves[i][1]

  try:
    print("Computer Moving ", s.board.san(move))
    s.board.push_san(s.board.san(move))
  except:
    print("error: invalid computer movement")
  

### ====== SERVER SIDE ====== ###
@app.route("/")
def index():
  ret = open("index.html").read()
  return ret.replace('start', s.board.fen())

@app.route("/move")
def move():
  if not s.board.is_game_over():
    source = int(request.args.get('from', default=''))
    target = int(request.args.get('to', default=''))
    promotion = True if request.args.get('promotion', default='') == 'true' else False

    move = s.board.san(chess.Move(source, target, promotion=chess.QUEEN if promotion else None))

  if move is not None and move != "":
    try:
      player_move(move)
      computer_move()
    except Exception:
      traceback.print_exc()
    response = app.response_class(
        response=s.board.fen(),
        status=200
        )
    return response
  else:
    response = app.response_class(
        response="game over",
        status=200
        )
    return response
  return index()

@app.route("/newgame")
def newgame():
  s.board.reset()
  response = app.response_class(
    response=s.board.fen(),
    status=200
  )
  return response


### ====== Driver ====== ###
if __name__ == "__main__":
  running = True
  print("Welcome to Deep Red")
  app.run(debug=True, port=5001)
