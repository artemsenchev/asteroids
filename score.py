import pygame

def displayScore(score):
    pygame.display.set_caption("Top Right Text")
    font = pygame.font.SysFont('Arial', 24)
    text = font.render('Top Right', True, (255, 255, 255))
    text_rect = text.get_rect()
    
    screen.blit(text, text_rect)