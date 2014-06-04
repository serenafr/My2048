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
		f = open(path, 'w')
		for i in self.__score_list:
			f.write(i.name)
			f.write('\n')
			f.write(str(i.score))
			f.write('\n')
		f.close()

	def load_scores(self, path):
		try:
			f = open(path, 'r')
		except IOError:
			return
		lines = f.readlines()
		for i in range(len(lines)):
			if i % 2 == 0:
				temp_name = lines[i].strip()
			else:
				temp_score = int((lines[i].strip()))
				self.__score_list.append(Score(temp_name, temp_score))
