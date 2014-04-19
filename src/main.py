import board

def main():
  board_object = board.Board(2)
  board_object.output()
  print '\n'
  next_step = ''
  while board_object.can_move():
    next_step = raw_input()
    board_object.move(next_step)
    board_object.output()

main()

