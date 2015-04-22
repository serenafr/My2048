import wx
import wx.lib.stattext as ST
import board

class My2048_wx(wx.Frame):
	def __init__(self, parent, id, title):
		super(My2048_wx, self).__init__(parent, title = title, 
			size = (300, 200))
		self.InitUI()

	def InitUI(self):
		SIZE = 4;

		'''panel_box is the container that contains all the widgets'''
		panel_box = wx.BoxSizer(wx.VERTICAL)

		'''header is the top parts which holds the name of the game,
		current score, and the best score'''
		header = wx.BoxSizer(wx.HORIZONTAL)		

		name = ST.GenStaticText(self, -1, label = '2048', 
			size = (100, 30))
		name.SetBackgroundColour((255, 0, 0))
		score = ST.GenStaticText(self, -1, label = '0')
		score.SetForegroundColour('white')
		score.SetBackgroundColour((187, 173, 160))
		best = ST.GenStaticText(self, -1, label = '0')
		best.SetForegroundColour('white')
		best.SetBackgroundColour((187, 173, 160))
		header.AddMany([name, score, best])
		panel_box.Add(header, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, 
			border = 10)

		sizer = wx.GridSizer(SIZE, SIZE)
		'''Set a list to store the numbers appear in different labels'''
		tile_list = []
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
		ST.GenStaticText(self, -1, label = text_list[i])'''
		label_list = []
		for i in range(0, SIZE * SIZE):
			label_list.append(ST.GenStaticText(self, -1, label = text_list[i]))
			label_list[i].SetBackgroundColour((238, 228, 218))
			sizer.Add(label_list[i])

		panel_box.Add(sizer, flag = wx.EXPAND|wx.TOP|wx.LEFT, 
			border = 10)

		self.SetSizer(panel_box)
		self.Show(True)

if __name__ == "__main__":
	app = wx.App()
	frame = My2048_wx(None, -1, '2048')
	app.MainLoop()
