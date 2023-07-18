from piece import Piece
from sprites import *
from settings import *

class Board:

	def __init__(self):
		self.rows = COLS
		self.cols = ROWS
		self.w = WIDTH // self.cols
		self.h = HEIGHT // self.rows
		self.board = [['' for i in range(self.cols)] for j in range(self.rows)]

	def place_pieces(self):
		'''for col in range(self.cols):
			self.board[1][col] = Piece('pawn','black',1,1,col)
			self.board[6][col] = Piece('pawn','white',1,6,col)'''
		self.board[4][1] = Piece('rook','black',5,4,1)
		self.board[4][3] = Piece('rook','black',5,4,3)
		self.board[0][0] = Piece('rook','black',5,0,0)
		self.board[0][7] = Piece('rook','black',5,0,7)
		self.board[7][0] = Piece('rook','white',5,7,0)
		self.board[7][7] = Piece('rook','white',5,7,7)
		self.board[0][1] = Piece('knight','black',3,0,1)
		self.board[0][6] = Piece('knight','black',3,0,6)
		self.board[7][1] = Piece('knight','white',3,7,1)
		self.board[7][6] = Piece('knight','white',3,7,6)
		self.board[0][2] = Piece('bishop','black',3,0,2)
		self.board[0][5] = Piece('bishop','black',3,0,5)
		self.board[7][2] = Piece('bishop','white',3,7,2)
		self.board[7][5] = Piece('bishop','white',3,7,5)
		self.board[0][3] = Piece('queen','black',9,0,3)
		self.board[7][3] = Piece('queen','white',9,7,3)
		self.board[0][4] = Piece('king','black',10000,0,4)
		self.board[7][4] = Piece('king','white',10000,7,4)

	def draw_pieces(self,display: object):
		for row in range(self.rows):
			for col in range(self.cols):
				pos = self.board[row][col]
				if pos != '':
					display.blit(sprites[(pos.color,pos.role)],(col * self.w,row * self.h))