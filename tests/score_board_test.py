import unittest
import sys
sys.path.append('../src')
import score_board

class Test_ScoreBoard(unittest.TestCase):

	def test_add_score(self):
		test_score_board = score_board.Score_Board()
		test_score_board.add_score(10, 'aaa')
		test_score_board.add_score(20, 'bbb')
		self.assertEqual(test_score_board.get_scores()[0].score, 20)
		self.assertEqual(test_score_board.get_scores()[1].score, 10)

	def test_up_to_ten(self):
		test_score_board = score_board.Score_Board()
		test_score_board.add_score(10, 'aaa')
		test_score_board.add_score(20, 'bbb')
		test_score_board.add_score(100, 'ccc')
		test_score_board.add_score(200, 'ddd')
		test_score_board.add_score(110, 'eee')
		test_score_board.add_score(220, 'fff')
		test_score_board.add_score(1, 'ggg')
		test_score_board.add_score(201, 'hhh')
		test_score_board.add_score(101, 'iii')
		test_score_board.add_score(202, 'jjj')
		test_score_board.add_score(150, 'kkk')
		test_score_board.add_score(250, 'lll')
		self.assertEqual(len(test_score_board.get_scores()), 10)

	def test_save_scores(self):
		test_score_board = score_board.Score_Board()
		test_score_board.add_score(10, 'aaa')
		test_score_board.add_score(20, 'bbb')
		test_score_board.save_scores('/tmp/testscore.txt')
		test_file = open('/tmp/testscore.txt', 'r')

		test_score_board2 = score_board.Score_Board()
		test_score_board2.load_scores('/tmp/testscore.txt')
		lst = test_score_board2.get_scores()

		self.assertEqual(test_score_board.get_scores(), lst)


if __name__ == '__main__':
  unittest.main()