import pygame
from settings import *
from board import Board

pygame.init()

class Game:

	def __init__(self):
		self.display = pygame.display.set_mode((WIDTH,HEIGHT))
		self.rows = 8
		self.cols = 8
		self.w = WIDTH // self.cols
		self.h = HEIGHT // self.rows
		self.board = Board()
		self.board.place_pieces()
		self.curr = None

	def run(self):
		run = True
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					x,y = pygame.mouse.get_pos()
					row,col = y // self.h,x // self.w
					if self.board.board[row][col] != '':
						self.curr = (row,col)

			self.display_board()
			self.board.draw_pieces(self.display)
			self.display_valid_moves()
			self.display_pointer(self.curr)
			pygame.display.update()

		pygame.quit()

	def display_board(self):
		for row in range(self.rows):
			for col in range(self.cols):
				if (row + col) % 2 == 0:
					pygame.draw.rect(self.display,(139,69,19),(col * self.w,row * self.h,self.w,self.h))
				else:
					pygame.draw.rect(self.display,(255,222,173),(col * self.w,row * self.h,self.w,self.h))

	def display_valid_moves(self):
		if self.curr:
			row,col = self.curr
			moves = self.board.board[row][col].return_valid_moves(self.board)
			for move in moves:
				row,col = move
				x,y = col * self.w + self.w // 2,row * self.h + self.w // 2
				pygame.draw.circle(self.display,(210,105,30),(x,y),self.w // 3)

	def display_pointer(self,pos):
		if self.curr:
			row,col = pos
			x,y = col * self.w,row * self.h
			pygame.draw.rect(self.display,(165,42,42),(x,y,self.w,self.h),5)

game = Game()
game.run()