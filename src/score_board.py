import os.path
import json

class Score(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def __repr__(self):
		return '%s: %d' % (self.name, self.score)

	def __eq__(self, other):
		return self.name == other.name and self.score == other.score


class Score_Board(object):
	def __init__(self):
		self.__score_list = []

	def sort_list(self):
		self.__score_list.sort(lambda x, y: x.score - y.score, reverse = True)

	def add_score(self, num, name):
		if len(self.__score_list) < 10:
			new_score = Score(name, num)
			self.__score_list.append(new_score)
			self.sort_list()
		elif num > self.__score_list[len(self.__score_list) - 1].score:
			self.__score_list[len(self.__score_list) - 1].score = num
			self.__score_list[len(self.__score_list) - 1].name = name
			self.sort_list()

	def get_scores(self):
		n_list = self.__score_list
		return n_list	

	def save_scores(self, path):
		dir_name = os.path.dirname(path)
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)
		f = open(path, 'w')
		jsonobj = [{"name" : i.name, "score" : i.score} for i in self.__score_list]
		jsonstr = json.dumps(jsonobj)
		f.write(jsonstr)
		f.close()

	def load_scores(self, path):
		self.__score_list = []
		try:
			f = open(path, 'r')
		except IOError:
			return
		jsonobj = json.load(f)
		self.__score_list = [Score(i["name"], i["score"]) for i in jsonobj]