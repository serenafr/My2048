print 'name in test:', __name__
from my2048 import generate_board, left_move
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

if __name__ == '__main__':
  test_left_move()
  print 'success'
