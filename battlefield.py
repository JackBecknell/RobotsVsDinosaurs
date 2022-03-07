from random import randint
from fleet import Fleet
from herd import Herd

#Our battlefield.
class Battlefield:
    def __init__(self):
        self.line_break = "******************************************************************\n"
        self.display_welcome()
        self.fleet_on_battlefield = Fleet()
        self.herd_on_battlefield = Herd()
        self.run_game()

    def display_welcome(self):
        print(f"Welcome Player! Quite the matchup Dinosaurs and Robots.\nOn our Robots side we have The Terminator!  Robo Cop! And Optimus Prime!\nAnd in the other corner we have the T-rex!, the Velociraptor!, and Spinosaurus!\nNow for the RULES:\n-Each Robot will choose 1 weapon to use all the way through the match.\n-While the Dinosaurs can switch up their attacks each time.\n-The damage for each attack is a secret so choose wisely.\n-Your robots and dinosaurs have a power/energy level and a health %, if either reaches 0 they won't be able to attack!\n\nLet's get started by giving our robots some weapons! Remember to choose well because they can't be changed.\nWhere as the dinosaurs get to choose a different attack each time!")

#Starts the game with a 'coin toss' by randomly choosing which side goes first, and continualy randomizes who goes next throughout the game.
    def run_game(self):
        self.game_complete = False
        self.coin_toss = 69
        print('One more thing, the turns in this game are randomized every time. A coin toss will dictate who gets to strike next!')
        while len(self.herd_on_battlefield.dinosaurs_in_herd) != 0 and len(self.fleet_on_battlefield.robots_in_fleet) != 0:
            self.coin_toss = randint(1,2)
            self.energy_check()
            self.check_health()
            if self.coin_toss == 1:
                self.coin_toss = 'Robots!'
            elif self.coin_toss == 2:
                self.coin_toss = 'Dinosaurs!'
            print(f'And after a quick coin toss it looks like the {self.coin_toss} will attack next.')
            if self.coin_toss == 'Robots!':
                self.robo_turn()
            else:
                self.dino_turn()
        print('Thanks for playing.')

#Master function for the dinosaurs turn that runs through all required functions before another coin toss.
    def dino_turn(self):
        self.user_chooses_dino_attacker()
        self.user_chooses_dino_attack()
        self.fleet_on_battlefield.robots_in_fleet[0].robo_health += self.attack_chosen[1]
        self.user_chooses_dino_for_turn.dino_energy_level -= 10
        self.battle(self.user_chooses_dino_for_turn , self.user_chooses_dino_for_turn.dino_name, self.attack_chosen,self.fleet_on_battlefield.robots_in_fleet[0].robo_name)
        self.energy_check()
        self.check_health()
        self.display_winners()

#Master function for the robots turn that runs through all require functions before another coin toss.
    def robo_turn(self):
        self.user_chooses_robo_attacker()
        self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health += self.user_chosen_robot.weapon_chosen[1]
        self.user_chosen_robot.robo_energy_level -= 10
        self.battle(self.user_chosen_robot , self.user_chosen_robot.robo_name, self.user_chosen_robot.weapon_chosen, self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name)
        self.energy_check()
        self.check_health()
        self.display_winners()

#Prints to the console relavent battle info for the users enjoyment.
    def battle(self,pass_full_attacking_robo_dino, pass_name_dino_or_robot_attacking, pass_weapon_or_attack, pass_dino_or_robot_being_attacked):
        if pass_weapon_or_attack[0] == 'Godzilla':
            print(f"{self.line_break}Well...After Godzilla had his way I don't think we'll be able to get enough pieces of {pass_dino_or_robot_being_attacked} for a burial.")
        elif pass_weapon_or_attack[0] == 'the Infinity Gauntlet':
            print(f"{self.line_break}*snap* Someone get a broom and a dustpan for whats left of {pass_dino_or_robot_being_attacked} over there.")
        elif pass_full_attacking_robo_dino in self.herd_on_battlefield.dinosaurs_in_herd:
            print(f"{self.line_break}{pass_name_dino_or_robot_attacking} just hit {pass_dino_or_robot_being_attacked} with a {pass_weapon_or_attack[0]} for {pass_weapon_or_attack[1]} health!")
        elif pass_full_attacking_robo_dino in self.fleet_on_battlefield.robots_in_fleet:
            print(f"{self.line_break}{pass_name_dino_or_robot_attacking} just used {pass_weapon_or_attack[0]} against {pass_dino_or_robot_being_attacked} for {pass_weapon_or_attack[1]} health!!")

#Gets called after every turn to check if health is above 0. If not that player gets deleted and a message prints to the console.
    def check_health(self):
        if len(self.fleet_on_battlefield.robots_in_fleet) == 0 or len(self.herd_on_battlefield.dinosaurs_in_herd) == 0:
            self.display_winners()
        elif self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health <= 0:
            print(f"{self.line_break}LOOK AT THAT BLOOD! {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} definitely isn't getting up again.")
            del self.herd_on_battlefield.dinosaurs_in_herd[0]
        elif self.fleet_on_battlefield.robots_in_fleet[0].robo_health <= 0:
            print(f"{self.line_break}What a hit {self.fleet_on_battlefield.robots_in_fleet[0].robo_name} Is down for the count!")
            del self.fleet_on_battlefield.robots_in_fleet[0]

#Gets called fter every turn to check if energy level is above 0. If not that player gets deleted and a message prints to the console.
    def energy_check(self):
        if self.herd_on_battlefield.dinosaurs_in_herd[0].dino_energy_level <= 0:
            print(f"{self.line_break}{self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} passes out from exhaustion")
            self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health = 0
        elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 2 and self.herd_on_battlefield.dinosaurs_in_herd[1].dino_energy_level <= 0:
            print(f"{self.line_break}{self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name} passes out from exhaustion")
            self.herd_on_battlefield.dinosaurs_in_herd[1].dino_health = 0
        elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 3 and self.herd_on_battlefield.dinosaurs_in_herd[2].dino_energy_level <= 0:
            print(f"{self.line_break}{self.herd_on_battlefield.dinosaurs_in_herd[2].dino_name} passes out from exhaustion")
            self.herd_on_battlefield.dinosaurs_in_herd[2].dino_health = 0
        elif self.fleet_on_battlefield.robots_in_fleet[0].robo_energy_level <= 0:
            print(f"{self.line_break}{self.fleet_on_battlefield.robots_in_fleet[0].robo_name} passes out from exhaustion")
            self.fleet_on_battlefield.robots_in_fleet[0].robo_health = 0
        elif len(self.fleet_on_battlefield.robots_in_fleet) == 2 and self.fleet_on_battlefield.robots_in_fleet[1].robo_energy_level <= 0:
            print(f"{self.line_break}{self.fleet_on_battlefield.robots_in_fleet[1].robo_name} passes out from exhaustion")
            self.fleet_on_battlefield.robots_in_fleet[1].robo_health = 0
        elif len(self.fleet_on_battlefield.robots_in_fleet) == 3 and self.fleet_on_battlefield.robots_in_fleet[2].robo_energy_level <= 0:
            print(f"{self.line_break}{self.fleet_on_battlefield.robots_in_fleet[2].robo_name} passes out from exhaustion")
            self.fleet_on_battlefield.robots_in_fleet[2].robo_health = 0

#Evaluates how many dinosaurs are left and allows the user to choose from them.
    def user_chooses_dino_attacker(self):
        self.dino_chosen = False
        while self.dino_chosen == False:
            if len(self.herd_on_battlefield.dinosaurs_in_herd) == 3:
                self.user_chooses_dino_for_turn = input(f"{self.line_break}-Dino's Turn-\nWho Gets to Attack?\nEnter '1' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_energy_level}% energy level.\nEnter '2' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_energy_level}% energy level.\nEnter '3' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_energy_level}% energy level.\n : ")
                if self.user_chooses_dino_for_turn in ['1','2' ,'3']:
                    self.dino_chosen = True
            elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 2:
                self.user_chooses_dino_for_turn = input(f"{self.line_break}-Dino's Turn-\nBE CAREFUL! YOU'RE DOWN TO 2 DINOS!\nEnter '1' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_energy_level}% energy level.\nEnter '2' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_energy_level}% energy level.\n : ")
                if self.user_chooses_dino_for_turn in ['1', '2']:
                    self.dino_chosen = True
            elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 1:
                self.user_chooses_dino_for_turn = input(f"{self.line_break}-Dino's Turn-\nThis is probably it...\nWell bud looks like your down to just {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name}. Press 1 followed by enter to make your last stand!\n : ")
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

#Allows the user to pick the next dino attack for the chosen dinosaur.  
    def user_chooses_dino_attack(self):
        self.dict_dino_atk_choice = {
            "attack_names" : ['Ad hominem', 'Dino-sit', 'Stomp','Slash','Bite','Godzilla'],
            "attack_values" : [ -1, -10, -20, -30, -40, -100],
            "console_print_response" : ['Ah yes, Ad hominem, some wounds never heal', 'Dino-sit, more humiliating than anything.',"Left foot, let's Stomp! Cha-cha now yall! Criss-Cross!!!", "Slash and watch em bleed..or leak.", "Bite! It is recomended you see a dentist after this.", "Instead of sending out your dinosaur to fight you ask GodZilla for a hand, it's VERY effective"]
        }
        self.attack_chosen = input(f"Alright player, what attack do you want {self.user_chooses_dino_for_turn.dino_name} to use next?\nType 1 for 'Ad hominem'.\nType 2 for 'Dino-sit'.\nType 3 for 'Stomp'.\nType 4 for 'Slash'.\nType 5 for 'Bite'.\nType 6 for 'Mystery attack'.\n : ")
        complete = False
        while complete == False:
            if self.attack_chosen == '1':
                print(self.dict_dino_atk_choice["console_print_response"][0])
                self.attack_chosen = [ self.dict_dino_atk_choice["attack_names"][0], self.dict_dino_atk_choice["attack_values"][0]]
                complete = True
            elif self.attack_chosen == '2':
                print(self.dict_dino_atk_choice["console_print_response"][1])
                self.attack_chosen = [self.dict_dino_atk_choice["attack_names"][1], self.dict_dino_atk_choice["attack_values"][1]]
                complete = True
            elif self.attack_chosen == '3':
                print(self.dict_dino_atk_choice["console_print_response"][2])
                self.attack_chosen = [self.dict_dino_atk_choice["attack_names"][2], self.dict_dino_atk_choice["attack_values"][2]]
                complete = True
            elif self.attack_chosen == '4':
                print(self.dict_dino_atk_choice["console_print_response"][3])
                self.attack_chosen = [self.dict_dino_atk_choice["attack_names"][3], self.dict_dino_atk_choice["attack_values"][3]]
                complete = True
            elif self.attack_chosen == '5':
                print(self.dict_dino_atk_choice["console_print_response"][4])
                self.attack_chosen = [self.dict_dino_atk_choice["attack_names"][4], self.dict_dino_atk_choice["attack_values"][4]]
                complete = True
            elif self.attack_chosen == '6':
                print(self.dict_dino_atk_choice["console_print_response"][5])
                self.attack_chosen = [self.dict_dino_atk_choice["attack_names"][5], self.dict_dino_atk_choice["attack_values"][5]]
                complete = True
            else:
                self.attack_chosen = input("Sorry kiddo, That wasn't a proper command.\n What attack do you want next?\nType 1 for 'Ad hominem'.\nType 2 for 'Dino-sit'.\nType 3 for 'Stomp'.\nType 4 for 'Slash'.\nType 5 for 'Bite'.\nType 6 for 'Ask GodZilla for a hand'.\n")

#Evaluates how many robots are left and allows the user to choose from them.
    def user_chooses_robo_attacker(self):
        self.robo_chosen = False
        while self.robo_chosen == False:
            if len(self.fleet_on_battlefield.robots_in_fleet) == 3:
                self.user_chosen_robot = input(f"{self.line_break}-Robo's Turn-\nWho Gets to Attack?\nEnter '1' for : {self.fleet_on_battlefield.robots_in_fleet[0].robo_name}, armed with {self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[0].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[0].robo_energy_level}% power level.\nEnter '2' for : {self.fleet_on_battlefield.robots_in_fleet[1].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[1].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[1].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[1].robo_energy_level}% power level.\nEnter '3' for : {self.fleet_on_battlefield.robots_in_fleet[2].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[2].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[2].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[2].robo_energy_level}% power level. : ")
                if self.user_chosen_robot in ['1' ,'2' ,'3']:
                    self.robo_chosen = True
            elif len(self.fleet_on_battlefield.robots_in_fleet) == 2:
                self.user_chosen_robot = input(f"{self.line_break}-Robo's Turn-\nBE CAREFUL! YOU'RE DOWN TO 2 ROBOS!\nEnter '1' for : {self.fleet_on_battlefield.robots_in_fleet[0].robo_name}, armed with {self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[0].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[0].robo_energy_level}% power level.\nEnter '2' for : {self.fleet_on_battlefield.robots_in_fleet[1].robo_name}, armed with a {self.fleet_on_battlefield.robots_in_fleet[1].weapon_chosen[0]}, at {self.fleet_on_battlefield.robots_in_fleet[1].robo_health} health, with {self.fleet_on_battlefield.robots_in_fleet[1].robo_energy_level}% power level.\n : ")
                if self.user_chosen_robot in ['1', '2']:
                    self.robo_chosen = True
            elif len(self.fleet_on_battlefield.robots_in_fleet) == 1:
                self.user_chosen_robot = input(f"{self.line_break}-Robo's Turn-\nThis is probably it...\nDamn, looks like your down to just {self.fleet_on_battlefield.robots_in_fleet[0].robo_name}. Give em HELL with your {self.fleet_on_battlefield.robots_in_fleet[0].weapon_chosen[0]}! It's {self.fleet_on_battlefield.robots_in_fleet[0].robo_health} Health and a dream.\nPress 1 followed by Enter to make your last stand! : ")
                if self.user_chosen_robot == '1':
                    self.robo_chosen = True
            else:
                print('Invalid Command')
        if self.user_chosen_robot =='1':
            self.user_chosen_robot = self.fleet_on_battlefield.robots_in_fleet[0]              
        elif self.user_chosen_robot =='2':
            self.user_chosen_robot = self.fleet_on_battlefield.robots_in_fleet[1]               
        elif self.user_chosen_robot =='3':
            self.user_chosen_robot = self.fleet_on_battlefield.robots_in_fleet[2]

#Evaluates how many members of a herd or fleet are left and prints a victory message to the team left standing.
    def display_winners(self):
        if len(self.fleet_on_battlefield.robots_in_fleet) == 0:
            print("GAME OVER!\nDINOSAURS RULE AGAIN!")
        elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 0:
            print("GAME OVER!\nTHE ROBOT'S ESTABLISH DOMINANCE!")


