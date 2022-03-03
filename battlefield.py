from random import randint
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet_on_battlefield = Fleet()
        self.herd_on_battlefield = Herd()

    def run_game(self):
        Fleet.create_fleet()
        Herd.create_herd()
        coin_toss = randint(0,2)

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_attack_options(self):
        pass

    def show_robo_attack_options(self):
        pass

    def display_winners(self):
        pass

