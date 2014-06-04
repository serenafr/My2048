import board
import score_board

SCORE_FILE_PATH = '/home/christine/.config/my2048/scores.conf' 
KEY_MOVE_MAP = {
  'a': board.Move.LEFT,
  'w': board.Move.UP,
  's': board.Move.DOWN,
  'd': board.Move.RIGHT,
}

def print_score_board(score_board):
  for i in score_board.get_scores():
    print i.name, ' ', i.score

def main():
  score_board_object = score_board.Score_Board()
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
  player = raw_input("Your score is %d, please enter your name: " % final_score)
  score_board_object.add_score(final_score, player)
  score_board_object.save_scores(SCORE_FILE_PATH)

main()

