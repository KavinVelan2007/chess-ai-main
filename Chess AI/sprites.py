import pygame
from settings import *

w = WIDTH // COLS
h = HEIGHT // ROWS

sprites = {
	('black','pawn'): pygame.transform.scale(pygame.image.load('assets/black_pawn.png'),(w,h)),
	('black','rook'): pygame.transform.scale(pygame.image.load('assets/black_rook.png'),(w,h)),
	('black','knight'): pygame.transform.scale(pygame.image.load('assets/black_knight.png'),(w,h)),
	('black','bishop'): pygame.transform.scale(pygame.image.load('assets/black_bishop.png'),(w,h)),
	('black','king'): pygame.transform.scale(pygame.image.load('assets/black_king.png'),(w,h)),
	('black','queen'): pygame.transform.scale(pygame.image.load('assets/black_queen.png'),(w,h)),
	('white','pawn'): pygame.transform.scale(pygame.image.load('assets/white_pawn.png'),(w,h)),
	('white','rook'): pygame.transform.scale(pygame.image.load('assets/white_rook.png'),(w,h)),
	('white','knight'): pygame.transform.scale(pygame.image.load('assets/white_knight.png'),(w,h)),
	('white','bishop'): pygame.transform.scale(pygame.image.load('assets/white_bishop.png'),(w,h)),
	('white','king'): pygame.transform.scale(pygame.image.load('assets/white_king.png'),(w,h)),
	('white','queen'): pygame.transform.scale(pygame.image.load('assets/white_queen.png'),(w,h))
}