from settings import *

class Piece:

	def __init__(self,role: str,color: str,score: int,row: int,col: int):
		self.role = role
		self.color = color
		self.row = row
		self.col = col
		self.rows = ROWS
		self.cols = COLS
		self.score = score
		self.first_move = True

	def return_valid_moves(self,board: object):
		moves = []
		if self.role == 'rook':
			if self.row < self.rows - 1:
				for row in range(self.row + 1,self.rows):
					if bool(board.board[row][self.col]):
						break
					else:
						moves.append((row,self.col))
			if self.row > 0:
				for row in range(self.row - 1,-1,-1):
					if bool(board.board[row][self.col]):
						break
					else:
						moves.append((row,self.col))
			if self.col < self.cols - 1:
				for col in range(self.col + 1,self.cols):
					if bool(board.board[self.row][col]):
						break
					else:
						moves.append((self.row,col))
			if self.col > 0:
				for col in range(self.col - 1,-1,-1):
					if bool(board.board[self.row][col]):
						break
					else:
						moves.append((self.row,col))
		return moves