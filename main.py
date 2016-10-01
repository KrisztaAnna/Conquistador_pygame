import pygame
from event import Event


class Grid(object):

    def __init__(self):
        pass


class Sidebar(object):

    def __init__(self, main):
        print(main.height)


class Main(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Conquistador')
        self.width = 1024
        self.height = 768
        self.screen = pygame.display.set_mode((self.width, self.height))  # , pygame.FULLSCREEN)
        self.screen.fill((0, 0, 0))

        conquiztador = State()

    def main_loop(self):
        print("Entering main loop...")
        while True:
            for event in pygame.event.get():
                Event.system_event_handler(event)


class State(object):

    def __init__(self):
        self.menu = Menu()
        self.game = Game()
        self.endscreen = Endscreen()

        self.game_state = self.game

    def start_game(self):
        self.game_state = self.game

    def end_game(self):
        self.game_state = self.endscreen

    def new_game(self):
        self.game_state = self.menu


class Menu(Main):

    def __init__(self):
        pass


class Game(Main):

    def __init__(self):
        super().__init__()
        self.grid = Grid()
        self.side_bar = Sidebar()



class Endscreen(Main):

    def __init__(self):
        pass





if __name__ == "__main__":
    state = State()
    # state.main_loop()
