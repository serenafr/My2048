import os.path
import json

class Score_Board(object):
	def __init__(self):
		self.__score_list = []

	def sort_list(self):
		self.__score_list.sort(lambda x, y: x - y, reverse = True)

	def add_score(self, num):
		if len(self.__score_list) < 10:
			self.__score_list.append(num)
			self.sort_list()
		elif num > self.__score_list[len(self.__score_list) - 1]:
			self.__score_list[len(self.__score_list) - 1] = num
			self.sort_list()

	def get_scores(self):
	#	self.load_scores(path)
		n_list = self.__score_list
		return n_list	

	def get_best_score(self):
		if len(self.__score_list) == 0:
			best = 0
		else:
			best = self.get_scores()[0]
		return best

	def save_scores(self, path):
		dir_name = os.path.dirname(path)
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)
		f = open(path, 'w')
		jsonobj = [i for i in self.__score_list]
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
		self.__score_list = [i for i in jsonobj]
