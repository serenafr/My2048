print 'name in test:', __name__
from my2048 import generate_board, left_move, BOARD_SIZE, move, output
print 'name in test after import:', __name__

def test_left_move():
  board = generate_board()
  board[0][0] = 2
  board[0][1] = 4
  board[0][2] = 2
  board = left_move(board)
  assert board[0][0] == 2
  assert board[0][1] == 4
  assert board[0][2] == 2
  
def test_left_move_unmoveable():
  board = generate_board()
  board[0][0] = 2
  new_board = copy_board(board)
  new_board = move(new_board, 'a')
  assert is_equal(board, new_board)

def copy_board(board):
  new_board = generate_board()
  for i in range(0, BOARD_SIZE):
    for j in range(0, BOARD_SIZE):
      new_board[i][j] = board[i][j]
  return new_board

def is_equal(lhs, rhs):
  for i in range(0, BOARD_SIZE):
    for j in range(0, BOARD_SIZE):
      if lhs[i][j] != rhs[i][j]:
	    return False
  return True

if __name__ == '__main__':
  test_left_move()
  test_left_move_unmoveable()
  print 'success'
