import wx
import wx.lib.stattext as ST
import board

class My2048_wx(wx.Frame):
	def __init__(self, parent, id, title):
		super(My2048_wx, self).__init__(parent, title = title, 
			size = (380, 300))
		self.InitUI()

	def InitUI(self):
		SIZE = 4;

		'''panel_box is the container that contains all the widgets'''
		panel_box = wx.BoxSizer(wx.VERTICAL)

		'''header is the top parts which holds the name of the game,
		current score, and the best score'''
		header = wx.BoxSizer(wx.VERTICAL)	

		'''upper_header contains three parts: game_name(2048), a boxsizer contains the current score information
		and another boxsizer contains the best score informaton
		All three parts are lined HORIZONTAL'''
		upper_header = wx.BoxSizer(wx.HORIZONTAL)
	
		game_name = ST.GenStaticText(self, -1, label = '2048', 
			size = (100, 30), style = wx.ALIGN_CENTRE)
		upper_header.Add(game_name, flag = wx.EXPAND|wx.RIGHT, border = 60)

		upper_header_score = wx.BoxSizer(wx.VERTICAL)
		score_str = ST.GenStaticText(self, -1, label = 'SCORE', size = (50, 20), style = wx.ALIGN_CENTRE)
		score_str.SetBackgroundColour((187, 173, 160))
		score = ST.GenStaticText(self, -1, label = '0', size = (50, 20), style = wx.ALIGN_CENTRE)
		score.SetForegroundColour('white')
		score.SetBackgroundColour((187, 173, 160))
		upper_header_score.AddMany([score_str, score])
		upper_header.Add(upper_header_score, flag = wx.EXPAND|wx.LEFT|wx.RIGHT, border = 10)

		upper_header_best = wx.GridSizer(2, 1)
		best_str = ST.GenStaticText(self, -1, label = 'BEST', size = (50, 20), style = wx.ALIGN_CENTRE)
		best_str.SetBackgroundColour((187, 173, 160))
		best = ST.GenStaticText(self, -1, label = '0', size = (50, 20), style = wx.ALIGN_CENTRE)
		best.SetForegroundColour('white')
		best.SetBackgroundColour((187, 173, 160))
		upper_header_best.AddMany([best_str, best])
		upper_header.Add(upper_header_best)
		
		header.Add(upper_header)

		'''lower_header contains a sub_title and a button that allows users to start a new game'''
		lower_header = wx.BoxSizer(wx.HORIZONTAL)

		sub_title = ST.GenStaticText(self, -1, label = 'Join the numbers and get to the 2048 tile!')
		lower_header.Add(sub_title, flag = wx.EXPAND|wx.RIGHT, border = 5)

		new_game_button = wx.Button(self, -1, label = 'NEW GAME')
		lower_header.Add(new_game_button)

		header.Add(lower_header)

		panel_box.Add(header, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, 
			border = 10)

		'''play_board is a container where all the tiles are put '''
		play_board = wx.GridSizer(SIZE, SIZE)
		'''Set a list to store the numbers appear in different labels'''
		tile_list = []
		'''Get tiles information frome board'''
		board_object = board.Board(2)
		tile_list = board_object.get_tiles()
		text_list = []
		for i in range(0, SIZE):
			for j in range(0, SIZE):
				if tile_list[i][j] == None:
					text_list.append('_')
				else:
					text_list.append(str(tile_list[i][j]))
		'''This list is used to store the wx labels with information
		ST.GenStaticText(self, -1, label = text_list[i])
		And put all the numbers from the board into the GUI'''
		label_list = []
		for i in range(0, SIZE * SIZE):
			label_list.append(ST.GenStaticText(self, -1, label = text_list[i],
				size = (60, 30), style = wx.ALIGN_CENTRE))
			label_list[i].SetBackgroundColour((238, 228, 218))
			play_board.Add(label_list[i])

		panel_box.Add(play_board, flag = wx.EXPAND|wx.TOP|wx.LEFT, 
			border = 10)

		'''User can use these keys to control the move and merge of the tile numbers'''
		ctrl_keys = wx.BoxSizer(wx.VERTICAL)

		up_box = wx.BoxSizer()
		up_button = wx.Button(self, -1, label = 'UP', size = (60, 30))
		up_box.Add(up_button, flag = wx.EXPAND|wx.LEFT, border = 110)
		ctrl_keys.Add(up_box)

		left_right_box = wx.GridSizer(1, 2)
		left_button = wx.Button(self, -1, label = 'LEFT', size = (60, 30))
		right_button = wx.Button(self, -1, label = 'RIGHT', size = (60, 30))
		left_right_box.Add(left_button, flag = wx.LEFT, border = 80)
		left_right_box.Add(right_button, flag = wx.RIGHT)
		ctrl_keys.Add(left_right_box)

		down_box = wx.BoxSizer()
		down_button = wx.Button(self, -1, label = 'DOWN', size = (60, 30))
		down_box.Add(down_button, flag = wx.EXPAND|wx.LEFT, border = 110)
		ctrl_keys.Add(down_box)


		panel_box.Add(ctrl_keys, flag = wx.EXPAND|wx.ALIGN_CENTRE|wx.TOP|wx.LEFT, border = 10)

		self.SetSizer(panel_box)
		self.Show(True)

if __name__ == "__main__":
	app = wx.App()
	frame = My2048_wx(None, -1, '2048')
	app.MainLoop()
