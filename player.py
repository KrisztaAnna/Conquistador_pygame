import pygame


class Player(object):

    ID = 0

    def __init__(self, color, position, maximum):
        self.color = color
        self.x = position[0]
        self.y = position[1]
        self.maximum = maximum
        Player.ID += 1
        self.name = 'Player ' + str(Player.ID)

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < self.maximum[0]:
            self.x += 1
        elif direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < self.maximum[1]:
            self.y += 1

    def __str__(self):
        return str("player.x: " + str(self.x) + " player.y: " + str(self.y))
