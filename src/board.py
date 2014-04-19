import random

class Move(object):
  LEFT = 'left'
  UP = 'up'
  RIGHT = 'right'
  DOWN = 'down'

class Board(object):
  
  def __init__(self, n_init_tiles):
    self.BOARD_SIZE = 4
    self.board_data = self.initialize_board(n_init_tiles)

  def generate_board(self):
    '''Generate a None board'''
    return [[None] * self.BOARD_SIZE for i in ' ' * self.BOARD_SIZE]

  def generate_line(self):
    '''Generate a line in board'''
    return [None] * self.BOARD_SIZE

  def initialize_board(self, n):
    '''Generate a board with n tiles whose value is not None'''
    base_num = self.generate_board()
    index_list = [[i, j] 
        for i in range(0, self.BOARD_SIZE) 
        for j in range(0, self.BOARD_SIZE)]
    for i in range(0, n):
      r_num = random.randint(0, len(index_list) - 1)
      temp = index_list[r_num]
      base_num[temp[0]][temp[1]] = 2
      index_list.remove(temp)
    return base_num
  
  def rotate(self, board):
    '''Rotate board 90 degree clockwise'''
    new_board = self.generate_board()
    for i in range(0, self.BOARD_SIZE):
      for j in range(0, self.BOARD_SIZE):
        new_board[i][j] = board[self.BOARD_SIZE - 1 - j][i]
    return new_board

  def get_through(self, line, a, b):
    '''return True if all the tiles between position a and position b are None'''
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
      
  def can_merge(self, line):
    '''return True if two occupied tiles can be merged into one'''
    for i in range(0, self.BOARD_SIZE):
      for j in range(0, self.BOARD_SIZE):
        if self.get_through(line, i, j) and line[i] == line[j]:
          return True
    return False

  def can_move_line(self, line):
    '''Return True if there is no valued tile between line[a] and line[b]'''
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
      if self.can_merge(line):
        return True
      else:
        for i in range(count, self.BOARD_SIZE):
          if line[i] != None:
            return True
      return False
      

  def can_move_left(self):
    for line in self.board_data:
      if self.can_move_line(line):
        return True
    return False
    
  def can_move_right(self):
    temp_board = self.generate_board()
    temp_board = self.rotate(self.rotate(self.board_data))
    for line in temp_board:
      if self.can_move_line(line):
        return True
    return False
    
  def can_move_up(self):
    temp_board = self.generate_board()
    temp_board = self.rotate(self.rotate(self.rotate(self.board_data)))
    for line in temp_board:
      if self.can_move_line(line):
        return True
    return False
    
  def can_move_down(self):
    temp_board = self.generate_board()
    temp_board = self.rotate(self.board_data)
    for line in temp_board:
      if self.can_move_line(line):
        return True
    return False
    
  def can_move(self):
    return self.can_move_left() or \
        self.can_move_right() or \
        self.can_move_up() or \
        self.can_move_down()
     
  def move_to_beginning(self, line):
    '''Move all the tiles with value to the beginning of the line'''
    count = 0
    line1 = self.generate_line()
    for i in line:
      if i != None:
        line1[count] = i
        count = count + 1
    return line1  

  def left_move(self, board):
    '''Move the tiles to the left, merge two tiles with the same value if they can_move()'''
    count = 0
    for line in board:
      occupied_tile = 0
      for i in line:
        if i != None:
          occupied_tile = occupied_tile + 1
      if occupied_tile == 1 and line[0] == None:
        board[count] = self.move_to_beginning(line)
      if occupied_tile > 1:
        if not self.can_merge(line):
          board[count] = self.move_to_beginning(line)
        else:
          status = [False] * self.BOARD_SIZE
          for i in range(0, self.BOARD_SIZE - 1):
            for j in range(i + 1, self.BOARD_SIZE):
              if self.get_through(line, i, j) and line[i] == line[j] and status[i] == False and status[j] == False:
                line[i] = line[i] + line[j]
                line[j] = None
                status[i] = True
                status[j] = True
          board[count] = self.move_to_beginning(line)
      count = count + 1
    return board

  def up_move(self, board):
    temp_board = self.generate_board()
    temp_board = self.rotate(self.rotate(self.rotate(board)))
    temp_board = self.left_move(temp_board)
    new_board = self.generate_board()
    new_board = self.rotate(temp_board)
    return new_board

  def right_move(self, board):
    temp_board = self.generate_board()
    temp_board = self.rotate(self.rotate(board))
    temp_board = self.left_move(temp_board)
    new_board = self.generate_board()
    new_board = self.rotate(self.rotate(temp_board))
    return new_board

  def down_move(self, board):
    temp_board = self.generate_board()
    temp_board = self.rotate(board)
    temp_board = self.left_move(temp_board)
    new_board = self.generate_board()
    new_board = self.rotate(self.rotate(self.rotate(temp_board)))
    return new_board

  KEY_MOVE_MAP = {
    Move.LEFT : left_move,
    Move.RIGHT : right_move,
    Move.UP : up_move,
    Move.DOWN : down_move,
  }
 
  def generate_tile(self, board):
    index_list = []
    for i in range(0, self.BOARD_SIZE):
      for j in range(0, self.BOARD_SIZE):
        if board[i][j] == None:
          temp = [i, j]
          index_list.append(temp)
    r_num = random.randint(0, len(index_list) - 1)
    pos = index_list[r_num]
    board[pos[0]][pos[1]] = 2
    return board

  def idle_tile(self, board):
    count = 0 
    for i in range(0, self.BOARD_SIZE):
      for j in range(0, self.BOARD_SIZE):
        if board[i][j] == None:
          count = count + 1
    return count
    
  def output(self):
    '''print board'''
    for i in self.board_data:
      s = []
      for j in i:
        if j == None:
          s.append('_'.center(4))
        else:
          s.append(str(j).center(4))
      print ' '.join(s) 

  def copy_board(self, board):
    new_board = self.generate_board()
    for i in range(0, self.BOARD_SIZE):
      for j in range(0, self.BOARD_SIZE):
        new_board[i][j] = board[i][j]
    return new_board

  def is_equal(self, lhs, rhs):
    for i in range(0, self.BOARD_SIZE):
      for j in range(0, self.BOARD_SIZE):
        if lhs[i][j] != rhs[i][j]:
          return False
    return True

  
  def move(self, move_action):
    '''Move the board to the direction specified by move_action
    
    move_action should be one of the values in Move enum'''
    old_board = self.copy_board(self.board_data)
    self.board_data = self.KEY_MOVE_MAP[move_action](self, self.board_data)
    if not self.is_equal(old_board, self.board_data):
      self.board_data = self.generate_tile(self.board_data)

