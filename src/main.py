import board

KEY_MOVE_MAP = {
  'a': board.Move.LEFT,
  'w': board.Move.UP,
  's': board.Move.DOWN,
  'd': board.Move.RIGHT,
}

def main():
  board_object = board.Board(2)
  board_object.output()
  print '\n'
  next_step = ''
  while board_object.can_move():
    next_step = raw_input()
    next_move = KEY_MOVE_MAP[next_step]
    board_object.move(next_move)
    print board_object.get_score()
    board_object.output()

main()

