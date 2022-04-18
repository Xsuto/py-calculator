import pygame

import settings

pygame.init()
FONT = pygame.font.Font(pygame.font.get_default_font(), settings.FONT_SIZE)
WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.CAPITATION)
