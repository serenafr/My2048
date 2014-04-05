import random

BOARD_SIZE = 4
#Generate a None board
def generate_board():
	return [[None] * BOARD_SIZE for i in ' ' * BOARD_SIZE]

#Generate a line in board
def generate_line():
	return [None] * BOARD_SIZE

#Generate a board with n tiles whose value is not None
def initiate_board(n):
	base_num = generate_board()
	index_list = [[i, j] for i in range(0, BOARD_SIZE) for j in range(0, BOARD_SIZE)]
	for i in range(0, n):
		r_num = random.randint(0, len(index_list) - 1)
		temp = index_list[r_num]
		base_num[temp[0]][temp[1]] = 2
		index_list.remove(temp)
	return base_num

#Rotate board 90 degree clockwise	
def rotate(board):
	new_board = generate_board()
	for i in range(0, BOARD_SIZE):
		for j in range(0, BOARD_SIZE):
			new_board[i][j] = board[BOARD_SIZE - 1 - j][i]
	return new_board

#return True if all the tiles between position a and position b are None
def get_through(line, a, b):
	gap = abs(a - b)
	if line[a] == None or line[b] == None:
		return False
	else:
		if gap == 0:
			return False
		elif gap == 1:
			return True
		else:
			for x in range(1, gap):
				if line[min(a, b) + x] != None:
					return False
			return True

#return True if two occupied tiles can be merged into one			
def can_merge(line):
	for i in range(0, BOARD_SIZE):
		for j in range(0, BOARD_SIZE):
			if get_through(line, i, j) and line[i] == line[j]:
				return True
	return False

#Return True if there is no valued tile between line[a] and line[b]
def can_move_line(line):
	count = 0
	for i in line:    # How many tiles are occupied in a line 
		if i != None:
			count = count + 1
	if count == 0:
		return False
	elif count == 1:
		if line[0] != None:
			return False
		return True
	else:
		if can_merge(line):
			return True
		else:
			for i in range(count, BOARD_SIZE):
				if line[i] != None:
					return True
		return False
		

def can_move_left(board):
	for line in board:
		if can_move_line(line):
			return True
	return False
	
def can_move_right(board):
	temp_board = generate_board()
	temp_board = rotate(rotate(board))
	for line in temp_board:
		if can_move_line(line):
			return True
	return False
	
def can_move_up(board):
	temp_board = generate_board()
	temp_board = rotate(rotate(rotate(board)))
	for line in temp_board:
		if can_move_line(line):
			return True
	return False
	
def can_move_down(board):
	temp_board = generate_board()
	temp_board = rotate(board)
	for line in temp_board:
		if can_move_line(line):
			return True
	return False
	
def can_move(board):
	return can_move_left(board) or can_move_right(board) or can_move_up(board) or can_move_down(board)
	
#Move all the tiles with value to the beginning of the line 
def move_to_beginning(line):
	count = 0
	line1 = generate_line()
	for i in line:
		if i != None:
			line1[count] = i
			count = count + 1
	return line1	

#Move the tiles to the left, merge two tiles with the same value if they can_move()
def left_move(board):
	count = 0
	for line in board:
		occupied_tile = 0
		for i in line:
			if i != None:
				occupied_tile = occupied_tile + 1
		if occupied_tile == 1 and line[0] == None:
			board[count] = move_to_beginning(line)
		if occupied_tile > 1:
			if not can_merge(line):
				board[count] = move_to_beginning(line)
			else:
				status = [False] * BOARD_SIZE
				for i in range(0, BOARD_SIZE - 1):
					for j in range(i + 1, BOARD_SIZE):
						if get_through(line, i, j) and line[i] == line[j] and status[i] == False and status[j] == False:
							line[i] = line[i] + line[j]
							line[j] = None
							status[i] = True
							status[j] = True
				board[count] = move_to_beginning(line)
		count = count + 1
	return board

def up_move(board):
	temp_board = generate_board()
	temp_board = rotate(rotate(rotate(board)))
	temp_board = left_move(temp_board)
	new_board = generate_board()
	new_board = rotate(temp_board)
	return new_board

def right_move(board):
	temp_board = generate_board()
	temp_board = rotate(rotate(board))
	temp_board = left_move(temp_board)
	new_board = generate_board()
	new_board = rotate(rotate(temp_board))
	return new_board

def down_move(board):
	temp_board = generate_board()
	temp_board = rotate(board)
	temp_board = left_move(temp_board)
	new_board = generate_board()
	new_board = rotate(rotate(rotate(temp_board)))
	return new_board

def generate_tile(board):
	index_list = []
	for i in range(0, BOARD_SIZE):
		for j in range(0, BOARD_SIZE):
			if board[i][j] == None:
				temp = [i, j]
				index_list.append(temp)
	r_num = random.randint(0, len(index_list) - 1)
	pos = index_list[r_num]
	board[pos[0]][pos[1]] = 2
	return board

def idle_tile(board):
	count = 0 
	for i in range(0, BOARD_SIZE):
		for j in range(0, BOARD_SIZE):
			if board[i][j] == None:
				count = count + 1
	return count
	
#print board
def output(board):
	for i in board:
		s = []
		for j in i:
			if j == None:
				s.append('_'.center(4))
			else:
				s.append(str(j).center(4))
		print ' '.join(s) 

#n = int(raw_input("Input a number: \n"))
print 'name in my2048.py:', __name__
if __name__ == '__main__':
	current_board = initiate_board(2)	
	occupied_tile = 2	
	output(current_board)
	print '\n'
	next_step = ''
	while can_move(current_board):
		next_step = raw_input()
		if next_step == 'a':
			current_board = left_move(current_board)
		if next_step == 'd':
			current_board = right_move(current_board)
		if next_step == 'w':
			current_board = up_move(current_board)
		if next_step == 's':
			current_board = down_move(current_board)
		
		output(current_board)
		print '\n'
		current_board = generate_tile(current_board)
		output(current_board)
