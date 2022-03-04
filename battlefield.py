from random import randint
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.display_welcome()
        self.fleet_on_battlefield = Fleet()
        self.herd_on_battlefield = Herd()
        self.run_game()

    def run_game(self):
        self.coin_toss = randint(1,2)
        if self.coin_toss == 1:
            self.coin_toss = 'Robots!'
        elif self.coin_toss == 2:
            self.coin_toss = 'Dinosaurs!'
        print(f'And after a quick coin toss it looks like the {self.coin_toss} will take the first turn!')
        if self.coin_toss == 'Robots!':
            self.robo_turn()
        else:
            self.dino_turn()

    def display_welcome(self):
        print(f"Welcome Player! Quite the matchup Dinosaurs and Robots.\n\nOn our Robots side we have {self.fleet_on_battlefield.robots_in_fleet[0].robo_name}!  {self.fleet_on_battlefield.robots_in_fleet[1].robo_name}! And {self.fleet_on_battlefield.robots_in_fleet[2].robo_name}!\n\nAnd in the other corner we have the {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name}!, the {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name}!, and {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_name}!\n\nNow for the rules! Each Robot will choose 1 weapon to use all the way through the match.\nWhile the Dinosaurs can switch it up each time.\n\nLet's get started by giving our robots some weapons!")

    def battle(self):
        pass

    def dino_turn(self):
        self.show_dino_attack_options()
        self.dino_turn_over = False
        while self.dino_turn_over != True:
            self.user_dino_attack_option = input("Enter here:")
            if self.user_dino_attack_option == 1 or self.user_dino_attack_option == '1':
                self.fleet_on_battlefield.robots_in_fleet[0].robo_health += self.herd_on_battlefield.dinosaurs_in_herd[0].attack_chosen[1] 
                self.dino_turn_over = True
            elif self.user_dino_attack_option == 2 or self.user_dino_attack_option == '2':
                self.fleet_on_battlefield.robots_in_fleet[0].robo_health += self.herd_on_battlefield.dinosaurs_in_herd[1].attack_chosen[1]
                self.dino_turn_over = True
            elif self.user_dino_attack_option == 3 or self.user_dino_attack_option == '3':
                self.fleet_on_battlefield.robots_in_fleet[0].robo_health += self.herd_on_battlefield.dinosaurs_in_herd[2].attack_chosen[1]
                self.dino_turn_over = True
            else:
                self.user_dino_attack_option = input("Invalid command. Try again:")
        self.check_health()
        self.robo_turn()    


    def robo_turn(self):
        self.show_robo_attack_options()
        self.robo_turn_over = False
        while self.robo_turn_over != True:
            self.user_robo_attack_option = input("Enter here:")  
            if self.user_robo_attack_option == 1 or self.user_robo_attack_option =='1':
                self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health += self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[1]
                self.robo_turn_over = True
            elif self.user_robo_attack_option == 2 or self.user_robo_attack_option =='2':
                self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health += self.fleet_on_battlefield.robots_in_fleet[1].weapon_chosen[1]
                self.robo_turn_over = True
            elif self.user_robo_attack_option == 3 or self.user_robo_attack_option =='3':
                self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health += self.fleet_on_battlefield.robots_in_fleet[2].weapon_chosen[1]
                self.robo_turn_over = True
            else:
                self.user_robo_attack_option = input("Invalid command. Try again:")
        self.check_health()
        self.dino_turn()

    #think about maybe breaking these up into three variables so that if 1 dies it doesn't show up as an option.
    def show_dino_attack_options(self):
        print(f"*************************************************************\n-Dino's Turn-\nYour Dino Team\nEnter '1' for : {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} ready to attack with {self.herd_on_battlefield.dinosaurs_in_herd[0].attack_chosen[0]} at {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health} heath, with {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_energy_level}% energy level.\nEnter '2' for : {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name} ready to attack with {self.herd_on_battlefield.dinosaurs_in_herd[1].attack_chosen[0]} at {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_health} heath, with {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_energy_level}% energy level.\nEnter '3' for : {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_name} ready to attack with {self.herd_on_battlefield.dinosaurs_in_herd[2].attack_chosen[0]} at {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_health} heath, with {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_energy_level}% energy level.\n")
    
    #think about maybe breaking these up into three variables so that if 1 dies it doesn't show up as an option.
    def show_robo_attack_options(self):
        print(f"*************************************************************\n-Robo's Turn-\nYour Robo Team\nEnter '1' for : {self.fleet_on_battlefield.robots_in_fleet[0].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[0].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[0].robo_energy_level}% power level.\nEnter '2' for : {self.fleet_on_battlefield.robots_in_fleet[1].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[1].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[1].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[1].robo_energy_level}% power level.\nEnter '3' for : {self.fleet_on_battlefield.robots_in_fleet[2].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[2].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[2].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[2].robo_energy_level}% power level.")

    def display_winners(self):
        pass

    def check_health(self):
        if self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health >= 0:
            print(f"Look at that BLOOD! {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} definitely isn't getting up again.")
            del self.herd_on_battlefield.dinosaurs_in_herd[0]
        elif self.fleet_on_battlefield.robots_in_fleet[0].robo_health >= 0:
            print(f"What a hit {self.fleet_on_battlefield.robots_in_fleet[0].robo_name} Is down for the count!")

