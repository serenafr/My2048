import random

class Board(object):
  
  def __init__(self):
    self.BOARD_SIZE = 4
    

  #Generate a None board
  def generate_board(self):
    return [[None] * self.BOARD_SIZE for i in ' ' * self.BOARD_SIZE]

  #Generate a line in board
  def generate_line(self):
    return [None] * self.BOARD_SIZE

  #Generate a board with n tiles whose value is not None
  def initiate_board(self, n):
    base_num = self.generate_board()
    index_list = [[i, j] for i in range(0, self.BOARD_SIZE) for j in range(0, self.BOARD_SIZE)]
    for i in range(0, n):
      r_num = random.randint(0, len(index_list) - 1)
      temp = index_list[r_num]
      base_num[temp[0]][temp[1]] = 2
      index_list.remove(temp)
    return base_num

  #Rotate board 90 degree clockwise  
  def rotate(self, board):
    new_board = self.generate_board()
    for i in range(0, self.BOARD_SIZE):
      for j in range(0, self.BOARD_SIZE):
        new_board[i][j] = board[self.BOARD_SIZE - 1 - j][i]
    return new_board

  #return True if all the tiles between position a and position b are None
  def get_through(self, line, a, b):
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
  def can_merge(self, line):
    for i in range(0, self.BOARD_SIZE):
      for j in range(0, self.BOARD_SIZE):
        if self.get_through(line, i, j) and line[i] == line[j]:
          return True
    return False

  #Return True if there is no valued tile between line[a] and line[b]
  def can_move_line(self, line):
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
      

  def can_move_left(self, board):
    for line in board:
      if self.can_move_line(line):
        return True
    return False
    
  def can_move_right(self, board):
    temp_board = self.generate_board()
    temp_board = self.rotate(self.rotate(board))
    for line in temp_board:
      if self.can_move_line(line):
        return True
    return False
    
  def can_move_up(self, board):
    temp_board = self.generate_board()
    temp_board = self.rotate(self.rotate(self.rotate(board)))
    for line in temp_board:
      if self.can_move_line(line):
        return True
    return False
    
  def can_move_down(board):
    temp_board = self.generate_board()
    temp_board = self.rotate(board)
    for line in temp_board:
      if self.can_move_line(line):
        return True
    return False
    
  def can_move(self, board):
    return self.can_move_left(board) or self.can_move_right(board) or self.can_move_up(board) or self.can_move_down(board)
    
  #Move all the tiles with value to the beginning of the line 
  def move_to_beginning(self, line):
    count = 0
    line1 = self.generate_line()
    for i in line:
      if i != None:
        line1[count] = i
        count = count + 1
    return line1  

  #Move the tiles to the left, merge two tiles with the same value if they can_move()
  def left_move(self, board):
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

  #KEY_MOVE_MAP = {
   # 'a' : left_move,
    #'d' : right_move,
    #'w' : up_move,
    #'s' : down_move,
  #}
    
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
    
  #print board
  def output(self, board):
    for i in board:
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

  
  def move(self, current_board, next_step):
    old_board = self.copy_board(current_board)
    if next_step == 'a':
      current_board = self.left_move(current_board)
    if next_step == 'd':
      current_board = self.right_move(current_board)
    if next_step == 'w':
      current_board = self.up_move(current_board)
    if next_step == 's':
      current_board = self.down_move(current_board)
    if not self.is_equal(old_board, current_board):
      current_board = self.generate_tile(current_board)
    return current_board