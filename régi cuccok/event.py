import pygame
from player import Player


class Event(object):

    @staticmethod
    def player_event_handler(event, player_1, player_2):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.move('left')

            elif event.key == pygame.K_a:
                player_2.move('left')
            elif event.key == pygame.K_RIGHT:
                player_1.move('right')
            elif event.key == pygame.K_d:
                player_2.move('right')
            elif event.key == pygame.K_UP:
                player_1.move('up')
            elif event.key == pygame.K_w:
                player_2.move('up')
            elif event.key == pygame.K_DOWN:
                player_1.move('down')
            elif event.key == pygame.K_s:
                player_2.move('down')

        return player_1, player_2

    @staticmethod
    def tile_event_handler(player, net):
        net[player.x][player.y].update_owner(player)

        return net
