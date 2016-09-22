import os
import sys
import pygame
from view import *
from pygame.locals import *
from player import Player
from event import Event
import time


class Main:

    def __init__(self, width=1000, height=600):
        pygame.init()
        pygame.display.set_caption('Conquistador')
        pygame.mixer.music.load('mountain_king.wav')
        pygame.mixer.music.play(loops=1, start=0.0)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))

        # -----------------------------------------
        # Menübe
        self.clock = pygame.time.Clock()
        self.counter, self.text = 60, '60'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont('comicsansms', 20)

        menu_width = 100
        menu_height = 50
        self.menu = Menu(menu_width, menu_height)
        # call this finally: Menu(menu_width, menu_height)
        # -----------------------------------------

        # -----------------------------------------
        # új class: GameField, ez kezeli a gridrajzolást és a infobarrajzolást is
        self.grid = Grid(self.screen, menu_width, menu_height, self.width-menu_width*2, self.height-menu_height, 10, 2)
        upper_left = (0, 0)
        bottom_right = (self.grid.net[-1][-1].x, self.grid.net[-1][-1].y)
        maximum = bottom_right
        # GameField.player1_position, GameField.player2_position
        # -----------------------------------------

        # -----------------------------------------
        # színeket a configfile-ba, a position a GameFieldből
        self.player_2 = Player((255, 255, 0), upper_left, maximum)
        self.player_1 = Player((80, 10, 220), bottom_right, maximum)
        # -----------------------------------------

    # -----------------------------------------
    # ez iszonyú ronda, ezt a menükezelőbe lesz szíves
    def highscore(self):
        score = self.grid.count_colors()
        self.screen.blit(self.font.render(str(self.player_1.name), True, (255, 255, 255)), (450, 50))
        self.screen.blit(self.font.render(str(score[self.player_1.color]), True, (255, 255, 255)), (495, 80))
        self.screen.blit(self.font.render(str(self.player_2.name), True, (255, 255, 255)), (450, 110))
        self.screen.blit(self.font.render(str(score[self.player_2.color]), True, (255, 255, 255)), (495, 140))
    # -----------------------------------------

    def main_loop(self):
        # status string: a játék éppen melyik része fut (menü, game, endscreen)
        game = True
        while True:
            if game:
                # -----------------------------------------
                for event in pygame.event.get():
                    # ezzel az eventtel meghívjuk az eventhandlert
                    # itt csak egy sor legyen
                    if event.type == pygame.QUIT:
                        game = False
                    self.player_1, self.player_2 = Event.player_event_handler(event, self.player_1, self.player_2)
                    self.grid.net = Event.tile_event_handler(self.player_1, self.grid.net)
                    self.grid.net = Event.tile_event_handler(self.player_2, self.grid.net)
                    self.grid.draw()
                    # -----------------------------------------
                    # ezt majd az infobarba rakd át
                    if event.type == pygame.USEREVENT:
                        self.counter -= 1
                        self.text = str(self.counter).rjust(3) if self.counter > 0 else 'Game Over!'
                        if self.text == 'Game Over!':
                            game = False
                    # -----------------------------------------

                else:
                    # -----------------------------------------
                    # ezt is a infobarba
                    pygame.draw.rect(self.screen, (0, 0, 0), [self.width/2, 10, 50, 30])
                    self.screen.blit(self.font.render(self.text, True, (255, 255, 255)), (self.width/2, 10))
                    self.screen.blit(self.font.render(self.player_2.name, True, (255, 255, 255)), (20, 20))
                    self.screen.blit(self.font.render(self.player_1.name, True, (255, 255, 255)), (self.width - 100, 20))

                    score = self.grid.count_colors()
                    pygame.draw.rect(self.screen, (0, 0, 0), [20, 50, 50, 50])
                    pygame.draw.rect(self.screen, (0, 0, 0), [self.width-100, 50, 50, 50])
                    self.screen.blit(self.font.render(str(score[self.player_2.color]), True, (255, 255, 255)), (20, 50))
                    self.screen.blit(self.font.render(str(score[self.player_1.color]), True, (255, 255, 255)), (self.width - 100, 50))
                    # -----------------------------------------

                    # screen.fillel "töroljük" a screent minden iteráció elején
                    pygame.display.flip()
                    self.clock.tick(60)
                    continue
                break

                pygame.display.update()
            else:
                self.screen.fill((0, 0, 0))
                self.highscore()
                pygame.display.update()
                time.sleep(3)
                quit()

            # while status == akármi:
                # fill
                # elágazások
                # update

if __name__ == "__main__":
    main = Main()
    main.main_loop()
    pygame.mixer.music.stop()  # ez ide nem kell
