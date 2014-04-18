import board

def main():
  board_object = board.Board()
  current_board = board_object.initiate_board(2)
  board_object.output(current_board)
  print '\n'
  next_step = ''
  while board_object.can_move(current_board):
    next_step = raw_input()
    current_board = board_object.move(current_board, next_step)
    board_object.output(current_board)
    
main()