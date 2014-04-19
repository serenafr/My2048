import sys
sys.path.append('../src')
import board

test_board = board.Board(2)
def test_left_move():
  board = test_board.generate_board()
  board[0][0] = 2
  board[0][1] = 4
  board[0][2] = 2
  board = test_board.left_move(board)
  assert board[0][0] == 2
  assert board[0][1] == 4
  assert board[0][2] == 2

def test_left_move_unmoveable():
  test_board = board.Board(0)
  test_board.board_data[0][0] = 2
  old_board = copy_board(test_board.board_data)
  test_board.move('a')
  assert is_equal(old_board, test_board.board_data)

def copy_board(board):
  new_board = test_board.generate_board()
  for i in range(0, test_board.BOARD_SIZE):
    for j in range(0, test_board.BOARD_SIZE):
      new_board[i][j] = board[i][j]
  return new_board

def is_equal(lhs, rhs):
  for i in range(0, test_board.BOARD_SIZE):
    for j in range(0, test_board.BOARD_SIZE):
      if lhs[i][j] != rhs[i][j]:
	    return False
  return True
  
test_left_move()
test_left_move_unmoveable()
print 'success'
