import wx
import wx.lib.stattext as ST
import board
import score_board

class My2048_wx(wx.Frame):

	def __init__(self, parent, id, title, size, board_object, score_board_object):
		super(My2048_wx, self).__init__(parent, title = title, 
			size = size)
		self.board_object = board_object
		self.score_board_object = score_board_object
		self.SIZE = self.board_object.BOARD_SIZE
		'''This list is used to store the wx labels with information
		ST.GenStaticText(self, -1, label = text_list[i])
		And put all the numbers from the board into the GUI'''
		self.__label_list = []
		self.__best_score = 0
		self.__current_score = 0
		self.Construct()

	def Construct(self):
		self.Bind(wx.EVT_CHAR_HOOK, self.arrow_key_ctrl)

		'''panel_box is the container that contains all the widgets'''
		self.panel_box = wx.BoxSizer(wx.VERTICAL)

		self.generate_header()

		'''play_board is a container where all the tiles are put '''
		self.play_board = wx.GridSizer(self.SIZE, self.SIZE)
		self.generate_playboard()


		self.SetSizer(self.panel_box)
		self.Show(True)


	def generate_header(self):
		'''header is the top parts which holds the name of the game,
		current score, and the best score'''
		self.header = wx.BoxSizer(wx.VERTICAL)	

		'''upper_header contains three parts: game_name(2048), a boxsizer contains the current score information
		and another boxsizer contains the best score informaton
		All three parts are lined HORIZONTAL'''
		self.upper_header = wx.BoxSizer(wx.HORIZONTAL)
	
		self.game_name = ST.GenStaticText(self, -1, label = '2048', 
			size = (100, 30), style = wx.ALIGN_CENTRE)
		self.upper_header.Add(self.game_name, flag = wx.EXPAND|wx.RIGHT, border = 60)

		self.upper_header_score = wx.BoxSizer(wx.VERTICAL)
		self.score_str = ST.GenStaticText(self, -1, label = 'SCORE', size = (50, 20), style = wx.ALIGN_CENTRE)
		self.score_str.SetBackgroundColour((187, 173, 160))
		self.score = ST.GenStaticText(self, -1, label = str(self.__current_score), size = (50, 20), style = wx.ALIGN_CENTRE)
		self.score.SetForegroundColour('white')
		self.score.SetBackgroundColour((187, 173, 160))
		self.upper_header_score.AddMany([self.score_str, self.score])
		self.upper_header.Add(self.upper_header_score, flag = wx.EXPAND|wx.LEFT|wx.RIGHT, border = 10)

		self.upper_header_best = wx.GridSizer(2, 1)
		self.best_str = ST.GenStaticText(self, -1, label = 'BEST', size = (50, 20), style = wx.ALIGN_CENTRE)
		self.best_str.SetBackgroundColour((187, 173, 160))
		self.__best_score = score_board_object.get_best_score()
		self.best = ST.GenStaticText(self, -1, label = str(self.__best_score), size = (50, 20), style = wx.ALIGN_CENTRE)
		self.best.SetForegroundColour('white')
		self.best.SetBackgroundColour((187, 173, 160))
		self.upper_header_best.AddMany([self.best_str, self.best])
		self.upper_header.Add(self.upper_header_best)
		
		self.header.Add(self.upper_header)

		'''lower_header contains a sub_title and a button that allows users to start a new game'''
		self.lower_header = wx.BoxSizer(wx.HORIZONTAL)

		self.sub_title = ST.GenStaticText(self, -1, label = 'Join the numbers and get to the 2048 tile!')
		self.lower_header.Add(self.sub_title, flag = wx.EXPAND|wx.RIGHT, border = 5)

		self.new_game_button = wx.Button(self, -1, label = 'NEW GAME')
		self.new_game_button.Bind(wx.EVT_BUTTON, self.new_game_button_click)
		self.lower_header.Add(self.new_game_button)

		self.header.Add(self.lower_header)

		self.panel_box.Add(self.header, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, 
			border = 10)

	def generate_playboard(self):
		'''Set a list to store the numbers appear in different labels'''
		tile_list = []
		text_list = []
		'''Get tiles information frome board'''
		tile_list = self.board_object.get_tiles()
		for i in range(0, self.SIZE):
			for j in range(0, self.SIZE):
				if tile_list[i][j] == None:
					text_list.append('_')
				else:
					text_list.append(str(tile_list[i][j]))

		for i in range(0, self.SIZE * self.SIZE):
			self.__label_list.append(ST.GenStaticText(self, -1, label = text_list[i], size = (60, 30), style = wx.ALIGN_CENTRE))
			self.__label_list[i].SetBackgroundColour((238, 228, 218))
			self.play_board.Add(self.__label_list[i], flag = wx.EXPAND|wx.RIGHT|wx.TOP, border = 10)

		self.panel_box.Add(
			self.play_board, flag = wx.EXPAND|wx.TOP|wx.LEFT, border = 10)

	def refresh(self):
		self.__current_score = board_object.get_score()
		self.score.SetLabel(str(self.__current_score))
		self.__best_score = score_board_object.get_best_score()
		if self.__current_score > self.__best_score:
			self.__best_score = self.__current_score
		self.best.SetLabel(str(self.__best_score))
		self.upper_header.Layout()

		'''Set a list to store the numbers appear in different labels'''
		tile_list = []
		text_list = []
		'''Get tiles information frome board'''
		tile_list = self.board_object.get_tiles()
		for i in range(0, self.SIZE):
			for j in range(0, self.SIZE):
				if tile_list[i][j] == None:
					text_list.append('_')
				else:
					text_list.append(str(tile_list[i][j]))

		for i in range(0, self.SIZE * self.SIZE):
			self.__label_list[i].SetLabel(text_list[i])
		self.play_board.Layout()

	def up_move(self):
		if board_object.can_move():
			board_object.move('up')
		self.refresh()

	def down_move(self):
		if board_object.can_move():
			board_object.move('down')
		self.refresh()

	def left_move(self):
		if board_object.can_move():
			board_object.move('left')
		self.refresh()

	def right_move(self):
		if board_object.can_move():
			board_object.move('right')
		self.refresh()

	def arrow_key_ctrl(self, event):
		if event.GetKeyCode() == wx.WXK_UP:
			self.up_move()
		elif event.GetKeyCode() == wx.WXK_DOWN:
			self.down_move()
		elif event.GetKeyCode() == wx.WXK_LEFT:
			self.left_move()
		elif event.GetKeyCode() == wx.WXK_RIGHT:
			self.right_move()
		else:
			event.Skip()

	def new_game_button_click(self, event):
		board_object.board_data = board_object.initialize_board(2)
		self.refresh()
		self.__current_score = 0
		self.score.SetLabel(str(self.__current_score))
		self.upper_header.Layout()


if __name__ == "__main__":
	app = wx.App()
	board_object = board.Board(2)
	score_board_object = score_board.Score_Board()
	frame = My2048_wx(None, -1, '2048', (380, 300), board_object, score_board_object)
	app.MainLoop()
