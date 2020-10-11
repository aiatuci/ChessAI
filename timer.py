from settings import *
import pygame_menu


class Timer:
    def __init__(self, time, pos):
        self.initial_time = time
        self.time = time
        self.pos = pos
        self.font = pygame.font.Font(pygame_menu.font.FONT_OPEN_SANS_BOLD, 18)

    def tick(self, dt):
        self.time -= dt

    def reset(self):
        self.time = self.initial_time

    def draw(self):
        mins, secs = divmod(self.time, 60)
        ms = divmod(self.time, 1000)[1]
        if self.time <= 10:
            s = f'{ms:.01f}'
        else:
            s = f'{int(mins):02}:{int(secs):02}'
        txt = self.font.render(s, True, SMALL_TEXT_COLOR)
        if self.pos == "top":
            pygame.draw.rect(SCREEN, BG_COLOR_LIGHT, [BOARD_X + BOARD_SIZE - TILE_SIZE, BOARD_Y - 36, TILE_SIZE, 28])
            SCREEN.blit(txt, (BOARD_X + BOARD_SIZE - TILE_SIZE + 8, BOARD_Y - 34))
        else:
            pygame.draw.rect(SCREEN, BG_COLOR_LIGHT,
                             [BOARD_X+BOARD_SIZE-TILE_SIZE, BOARD_Y+BOARD_SIZE+8, TILE_SIZE, 28])
            SCREEN.blit(txt, (BOARD_X+BOARD_SIZE-TILE_SIZE+8, BOARD_Y+BOARD_SIZE+10))
