import pygame



def score(Ball, screen, WHITE, score_A,score_B ):


            font = pygame.font.Font(None, 74)
            text = font.render(str(score_A), 1, WHITE)
            screen.blit(text, (250, 10))
            text = font.render(str(score_B), 1, WHITE)
            screen.blit(text, (710, 10))