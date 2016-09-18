from main import *
import random
import time
from player import Player


class Tile():

    def __init__(self, x, y, owner):
        self.owner = owner
        self.x = x
        self.y = y
        if self.owner:
            self.color = owner.color
        else:
            self.color = (105, 105, 105)

    def __str__(self):
        return str("x: " + str(self.x) + " y: " + str(self.y))

    def update_owner(self, owner):
        self.owner = owner
        self.color = owner.color


class Grid():

    def __init__(self, screen, start_width, start_height, width, height, piece_count, margin):
        self.screen = screen
        self.start_width = start_width
        self.start_height = start_height
        self.net = []
        self.margin = margin

        if width > height:
            self.size = height//piece_count
            height = self.size
            piece_count_column = width//self.size
            self.residual = (width % self.size)/2
            piece_count_row = piece_count
        else:
            self.size = width//piece_count
            width = self.size
            piece_count_row = height//self.size
            piece_count_column = piece_count

        for row in range(piece_count_column):
            self.net.append([])
            for column in range(piece_count_row):
                self.net[row].append(Tile(row, column, None))

    def draw(self):
        for row in self.net:
            for column in row:
                pygame.draw.rect(self.screen, column.color, [
                    column.x*(self.size) + self.start_width + self.residual,
                    column.y*(self.size) + self.start_height,
                    self.size-self.margin, self.size-self.margin
                    ])

    def count_colors(self):
        owners = {}
        for row in self.net:
            for column in row:
                try:
                    owners[column.owner.color] = owners.get(column.owner.color, 0) + 1
                except AttributeError:
                    owners[None] = owners.get(None, 0) + 1
        return owners


    def __str__(self):
        return str(self.x)


class Menu():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        counter, text = 10, '10'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont('Consolas', 30)
