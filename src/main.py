import board
import score_board
from os.path import expanduser


SCORE_FILE_PATH = expanduser('~/.config/my2048/scores.conf')
KEY_MOVE_MAP = {
  'a': board.Move.LEFT,
  'w': board.Move.UP,
  's': board.Move.DOWN,
  'd': board.Move.RIGHT,
}

def print_score_board(score_board):
  for i in score_board.get_scores():
    print i

if __name__ == "__main__":
  score_board_object = score_board.Score_Board()
  while True:
    score_board_object.load_scores(SCORE_FILE_PATH)
    print_score_board(score_board_object)
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
    final_score = board_object.get_score()
    score_board_object.add_score(final_score)
    score_board_object.save_scores(SCORE_FILE_PATH)


