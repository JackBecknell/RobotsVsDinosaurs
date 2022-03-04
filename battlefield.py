from random import randint
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot

class Battlefield:
    def __init__(self):
        self.display_welcome()
        self.fleet_on_battlefield = Fleet()
        self.herd_on_battlefield = Herd()
        self.run_game()
#Starts the game by randomly choosing which side goes first
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
#OPENING DISPLAY MESSAGE
    def display_welcome(self):
        print(f"Welcome Player! Quite the matchup Dinosaurs and Robots.\nOn our Robots side we have The Terminator!  Robo Cop! And Optimus Prime!\nAnd in the other corner we have the T-rex!, the Velociraptor!, and Spinosaurus!\nNow for the RULES:\n-Each Robot will choose 1 weapon to use all the way through the match.\n-While the Dinosaurs can switch up their attacks each time.\n-The damage for each attack is a secret so choose wisely.\n-Your robots and dinosaurs have a power/energy level and a health %, if either reaches 0 they won't be able to attack!\n\nLet's get started by giving our robots some weapons! Remember to choose well because they can't be changed.\nWhere as the dinosaurs get to choose a different attack each time!")

    def battle(self, pass_dino_or_robot_attacking, pass_weapon_or_attack, pass_dino_or_robot_being_attacked):
        if pass_dino_or_robot_attacking in self.herd_on_battlefield.dinosaurs_in_herd:
            print(f"{pass_dino_or_robot_attacking} just hit {pass_dino_or_robot_being_attacked} with a {pass_weapon_or_attack}!")
        elif pass_dino_or_robot_attacking in self.fleet_on_battlefield.robots_in_fleet:
            print(f"{pass_dino_or_robot_attacking} just used {pass_weapon_or_attack} against {pass_dino_or_robot_being_attacked}!")

#Allows user to pick dinosaur and attack for the turn before checking health and giving the robots another turn.
    def dino_turn(self):
        self.show_remaining_dino_options()
        self.user_chooses_current_dino_attack()
        self.fleet_on_battlefield.robots_in_fleet[0].robo_health += self.attack_chosen[1]
        self.user_chooses_dino_for_turn.dino_energy_level -= 10
        self.battle(self.user_chooses_dino_for_turn.dino_name, self.attack_chosen[0],self.fleet_on_battlefield.robots_in_fleet[0].robo_name)
        self.check_health()
        self.display_winners()
        self.robo_turn()

#Allows the user to pick the next dino attack for the chosen dinosaur   
    def user_chooses_current_dino_attack(self):
        self.dinosaur_attack_choices = [('Ad hominem', -1), ('Dino-sit', -10), ('Stomp', -20), ('Slash', -30), ('Bite', -40), ('Godzilla', -100)]
        self.attack_chosen = input(f"Alright gamer, what attack do you want {self.user_chooses_dino_for_turn.dino_name} to use next?\nType 1 for 'Ad hominem'.\nType 2 for 'Dino-sit'.\nType 3 for 'Stomp'.\nType 4 for 'Slash'.\nType 5 for 'Bite'.\nType 6 for 'Mystery attack'.\n")
        complete = False
        while complete == False:
            if self.attack_chosen == '1':
                print('Ah yes, Ad hominem, some wounds never heal')
                self.attack_chosen = [self.dinosaur_attack_choices[1][0],self.dinosaur_attack_choices[0][1]]
                complete = True
            elif self.attack_chosen == '2':
                print('Dino-sit, more humiliating than anything.')
                self.attack_chosen = [self.dinosaur_attack_choices[1][0], self.dinosaur_attack_choices[1][1]]
                complete = True
            elif self.attack_chosen == '3':
                print("Left foot, let's Stomp! Cha-cha now yall! Criss-Cross!!!")
                self.attack_chosen = [self.dinosaur_attack_choices[2][0], self.dinosaur_attack_choices[2][1]]
                complete = True
            elif self.attack_chosen == '4':
                print("Slash and watch em bleed..or leak.")
                self.attack_chosen = [self.dinosaur_attack_choices[3][0], self.dinosaur_attack_choices[3][1]]
                complete = True
            elif self.attack_chosen == '5':
                print("Bite! It is recomended you see a dentist after this.")
                self.attack_chosen = [self.dinosaur_attack_choices[4][0], self.dinosaur_attack_choices[4][1]]
                complete = True
            elif self.attack_chosen == '6':
                print(f"Instead of sending {self.user_chooses_dino_for_turn.dino_name} to fight you ask GodZilla for a hand, it's VERY effective")
                self.attack_chosen = [self.dinosaur_attack_choices[5][0], self.dinosaur_attack_choices[5][1]]
                complete = True
            else:
                self.attack_chosen = input("Sorry kiddo, That wasn't a proper command.\n What attack do you want next?\nType 1 for 'Ad hominem'.\nType 2 for 'Dino-sit'.\nType 3 for 'Stomp'.\nType 4 for 'Slash'.\nType 5 for 'Bite'.\nType 6 for 'Ask GodZilla for a hand'.\n")

#Evaluates how many dinosaurs are left and based off the amount stores a value from an input into 'self.user_choose_dino_from_turn' the script then takes the number within the string and will change the value of the variable to the inidcated dinosaur to conduct the next attack.
    def show_remaining_dino_options(self):
        self.dino_chosen = False
        while self.dino_chosen == False:
            if len(self.herd_on_battlefield.dinosaurs_in_herd) == 3:
                self.user_chooses_dino_for_turn = input(f"*************************************************************\n-Dino's Turn-\nWho Gets to Attack?\nEnter '1' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_energy_level}% energy level.\nEnter '2' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_energy_level}% energy level.\nEnter '3' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_energy_level}% energy level.\n")
                if self.user_chooses_dino_for_turn == '1' or self.user_chooses_dino_for_turn == '2' or self.user_chooses_dino_for_turn == '3':
                    self.dino_chosen = True
            elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 2:
                self.user_chooses_dino_for_turn = input(f"*************************************************************\n-Dino's Turn-\nBE CAREFUL! YOU'RE DOWN TO 2 DINOS!\nEnter '1' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_energy_level}% energy level.\nEnter '2' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_energy_level}% energy level.\n")
                if self.user_chooses_dino_for_turn == '1' or self.user_chooses_dino_for_turn == '2':
                    self.dino_chosen = True
            elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 1:
                self.user_chooses_dino_for_turn = input(f"*************************************************************\n-Dino's Turn-\nThis is probably it...\nWell bud looks like your down to just {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name}. Press 1 followed by enter to make your last stand!")
                if self.user_chooses_dino_for_turn == '1':
                    self.dino_chosen = True
            else:
                print('Invalid Command')
        if self.user_chooses_dino_for_turn == '1':
            self.user_chooses_dino_for_turn = self.herd_on_battlefield.dinosaurs_in_herd[0]
        elif self.user_chooses_dino_for_turn == '2':
            self.user_chooses_dino_for_turn = self.herd_on_battlefield.dinosaurs_in_herd[1]
        elif self.user_chooses_dino_for_turn == '3':
            self.user_chooses_dino_for_turn = self.herd_on_battlefield.dinosaurs_in_herd[2]

#Based off the stored value in 'self.user_chosen_robo_attack' It will take the chosen robots weapon damage and apply it to the enemies health
    def robo_turn(self):
        self.show_robo_attack_options()
        self.robo_turn_over = False
        while self.robo_turn_over != True:  
            if self.user_chosen_robo_attack =='1':
                self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health += self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[1]
                self.fleet_on_battlefield.robots_in_fleet[0].robo_energy_level -= 10
                self.robo_turn_over = True
                self.battle( self.fleet_on_battlefield.robots_in_fleet[0].robo_name, self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[0], self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name )
            elif self.user_chosen_robo_attack =='2':
                self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health += self.fleet_on_battlefield.robots_in_fleet[1].weapon_chosen[1]
                self.fleet_on_battlefield.robots_in_fleet[1].robo_energy_level -= 10
                self.robo_turn_over = True
                self.battle(self.fleet_on_battlefield.robots_in_fleet[1].robo_name, self.fleet_on_battlefield.robots_in_fleet[1].weapon_chosen[0], self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name)
            elif self.user_chosen_robo_attack =='3':
                self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health += self.fleet_on_battlefield.robots_in_fleet[2].weapon_chosen[1]
                self.fleet_on_battlefield.robots_in_fleet[2].robo_energy_level -= 10
                self.robo_turn_over = True
                self.battle(self.fleet_on_battlefield.robots_in_fleet[2].robo_name, self.fleet_on_battlefield.robots_in_fleet[2].weapon_chosen[0], self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name)
        self.check_health()
        self.display_winners()
        self.dino_turn()

#Evaluates how many robots are left and gives the user updated choices depending on how many there are.
    def show_robo_attack_options(self):
        self.user_selected_robo_attack_option = False
        while self.user_selected_robo_attack_option == False:
            if len(self.fleet_on_battlefield.robots_in_fleet)  == 3:
                self.user_chosen_robo_attack = input(f"*************************************************************\n-Robo's Turn-\nWho Gets to Attack?\nEnter '1' for : {self.fleet_on_battlefield.robots_in_fleet[0].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[0].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[0].robo_energy_level}% power level.\nEnter '2' for : {self.fleet_on_battlefield.robots_in_fleet[1].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[1].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[1].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[1].robo_energy_level}% power level.\nEnter '3' for : {self.fleet_on_battlefield.robots_in_fleet[2].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[2].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[2].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[2].robo_energy_level}% power level.")
                if self.user_chosen_robo_attack == '1' or self.user_chosen_robo_attack == '2' or self.user_chosen_robo_attack == '3':
                    self.user_selected_robo_attack_option = True
                else:
                    print('Invalid Command')
            elif len(self.fleet_on_battlefield.robots_in_fleet)  == 2:
                self.user_chosen_robo_attack = input(f"*************************************************************\n-Robo's Turn-\nBE CAREFUL! YOU'RE DOWN TO 2 ROBOS!\nEnter '1' for : {self.fleet_on_battlefield.robots_in_fleet[0].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[0].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[0].robo_energy_level}% power level.\nEnter '2' for : {self.fleet_on_battlefield.robots_in_fleet[1].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[1].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[1].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[1].robo_energy_level}% power level.\n")
                if self.user_chosen_robo_attack == '1' or self.user_chosen_robo_attack == '2' or self.user_chosen_robo_attack == '3':
                    self.user_selected_robo_attack_option = True
                else:
                    print('Invalid Command')
            elif len(self.fleet_on_battlefield.robots_in_fleet)  == 1:
                self.user_chosen_robo_attack = input(f"*************************************************************\n-Robo's Turn-\nThis is probably it...\nDamn, looks like your down to just {self.fleet_on_battlefield.robots_in_fleet[0].robo_name}. Give em HELL with your {self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[0]}! Press 1 followed by Enter to make your last stand!\n")
                if self.user_chosen_robo_attack == '1' or self.user_chosen_robo_attack == '2' or self.user_chosen_robo_attack == '3':
                    self.user_selected_robo_attack_option = True
                else:
                    print('Invalid Command')

#Not yet fully hashed out...
    def display_winners(self):
        if len(self.fleet_on_battlefield.robots_in_fleet) == 0:
            print("GAME OVER!\nDINOSAURS RULE AGAIN!")
        elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 0:
            print("GAME OVER!\nTHE ROBOT'S ESTABLISH DOMINANCE!")

#Gets called after every turn to see if anyone died as well as to print a message if so.
    def check_health(self):
        if self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health <= 0:
            print(f"*************************************************************\nLOOK AT THAT BLOOD! {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} definitely isn't getting up again.")
            del self.herd_on_battlefield.dinosaurs_in_herd[0]
        elif self.fleet_on_battlefield.robots_in_fleet[0].robo_health <= 0:
            print(f"*************************************************************\nWhat a hit {self.fleet_on_battlefield.robots_in_fleet[0].robo_name} Is down for the count!")
            del self.fleet_on_battlefield.robots_in_fleet[0]

