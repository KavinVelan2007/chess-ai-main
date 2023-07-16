import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill((230, 185, 133))
squares = [(x,y) for y in range(8) for x in range(8)]
pygame.display.set_caption('Chess')
icon = pygame.image.load('chess_icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
main_surface1 = pygame.Surface((100,100))
main_surface1.fill((227, 141, 41))
b_bishop = pygame.image.load('1.png')
w_bishop = pygame.image.load('2.png')
b_king = pygame.image.load('3.png')
w_king = pygame.image.load('4.png')
b_knight = pygame.image.load('5.png')
w_knight = pygame.image.load('6.png')
b_pawn = pygame.image.load('7.png')
w_pawn = pygame.image.load('8.png')
b_queen = pygame.image.load('9.png')
w_queen = pygame.image.load('10.png')
b_rook = pygame.image.load('11.png')
w_rook = pygame.image.load('12.png')
position = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1,), (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6),]
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for (a,b) in squares:
        if (a+b)%2 == 1:
            screen.blit(main_surface1, (a*100,b*100))
    for (a,b) in position:
        c = (a*100 + 20, b*100 + 20)
        if (a,b) == position[0] or (a,b) == position[7]:
            screen.blit(b_rook, c)
        elif (a,b) == position[1] or (a,b) == position[6]:
            screen.blit(b_knight, c)
        elif (a,b) == position[2] or (a,b) == position[5]:
            screen.blit(b_bishop,c)
        elif (a,b) == position[3]:
            screen.blit(b_queen, c)
        elif (a,b) == position[4]:
            screen.blit(b_king, c)
        elif (a,b) in position[8:16]:
            screen.blit(b_pawn, c)
        elif (a,b) == position[16] or (a,b) == position[23]:
            screen.blit(w_rook, c)
        elif (a,b) == position[17] or (a,b) == position[22]:
            screen.blit(w_knight, c)
        elif (a,b) == position[18] or (a,b) == position[21]:
            screen.blit(w_bishop,c)
        elif (a,b) == position[19]:
            screen.blit(w_queen, c)
        elif (a,b) == position[20]:
            screen.blit(w_king, c)
        elif (a,b) in position[24:32]:
            screen.blit(w_pawn, c)
    pygame.display.update()
    clock.tick()
