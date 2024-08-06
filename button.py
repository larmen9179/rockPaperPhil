import pygame as py
from settings import *
from system import *

py.init()

font = py.font.Font("assets/fonts/mainFont.ttf", fontSize)


class Button:
    def __init__(self, text, position, width, height, default_color, clicked_color):
        self.text = text
        self.position = position
        self.width = width
        self.height = height
        self.default_color = default_color
        self.clicked_color = clicked_color
        self.color = default_color
        self.rect = py.Rect(position, (width, height))

    def draw(self, screen):
        py.draw.rect(screen, self.color, self.rect)
        if self.text != "spill":
            text_surface = font.render(self.text, True, "black")
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def handleEvent(self, event):
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True, self.text
            else:
                return False, self.text