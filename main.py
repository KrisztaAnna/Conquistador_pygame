import pygame


class Main(object):

    def __init__(self):
        conquiztador = State()

    def main_loop(self):
        while True:
            print("megy a játék")


class State(object):

    def __init__(self):
        self.menu = Menu()
        self.game = Game()
        self.endscreen = Endscreen()

        self.game_state = self.menu

    def start_game(self):
        self.game_state = self.game

    def end_game(self):
        self.game_state = self.endscreen

    def new_game(self):
        self.game_state = self.menu


class Menu(object):

    def __init__(self):
        pass


class Game(object):

    def __init__(self):
        pass


class Endscreen(object):

    def __init__(self):
        pass


if __name__ == "__main__":
    main = Main()
    main.main_loop()
