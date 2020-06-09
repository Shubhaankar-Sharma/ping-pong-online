import pygame
from paddle import Paddle
from ball import Ball
from network import Network
from scoreboard import score
import sys, os
##new code remove
def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
##new
# initialization (do this in every game pygame.init())
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# creating a screen
screen = pygame.display.set_mode((960, 720))

# title and icon
pygame.display.set_caption("Pong by shubhaankar")
icon = pygame.image.load(resource_path('pong.png')) # new
pygame.display.set_icon(icon)

# background
background = pygame.image.load(resource_path('background.png')) # new

# creating list for sprites
sprites_lists = pygame.sprite.Group()

# Adding the paddles to the list



"""Defining the tuple for the position relay"""




# loop for quitting

def main():
        clock =  pygame.time.Clock()
        scoreA = 0
        scoreB = 0
        running = True
        n = Network()
        pos = []

        while n.getP() is None:
            _ = 0
        player_1_list = n.getP()
        P = Paddle(player_1_list[0][0],player_1_list[0][1],player_1_list[0][2])

        P.rect.x = player_1_list[1][0]
        P.rect.y = player_1_list[1][1]
        pos.append(player_1_list[1])
        p2 = Paddle(RED, 20, 90)
        sprites_lists.add(P)
        sprites_lists.add(p2)

        ball = Ball(WHITE, 20, 20,player_1_list[2][0],player_1_list[2][1])
        ball.rect.x = 472
        ball.rect.y = 350
        sprites_lists.add(ball)
        while running:


                    p2_pos = n.send(pos)
                    print(p2_pos)
                    if type(p2_pos) == list:
                        p2.rect.x = p2_pos[0]
                        p2.rect.y = p2_pos[1]
                    for event in pygame.event.get():

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False

                    P.paddle_movement()

                    ball.movement(P, p2, scoreA, scoreB)
                    if ball.rect.x >= 950:
                        scoreA += 1
                    if ball.rect.x <= 0:
                        scoreB += 1
                    sprites_lists.update()

                    screen.blit(background, (0, 0))
                    sprites_lists.draw(screen)
                    # Score
                    pos = [[P.rect.x,P.rect.y]]

                    score(ball,screen,WHITE,scoreA,scoreB)
                    pygame.display.flip()
                    clock.tick(120)

main()
pygame.quit()
