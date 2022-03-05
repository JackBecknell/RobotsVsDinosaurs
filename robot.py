from weapon import Weapon

class Robot:
    def __init__(self, pass_name):
        self.robo_name = pass_name
        self.robo_health = 100
        self.robo_energy_level = 100
        self.weapons_dict = {
            'Fly Swatter' : ('a Fly Swatter', -1),
            'Spatula' : ('a Spatula', -10),
            'Battle Axe' : ('a Battle Axe', -20),
            'Minigun' : ('a Minigun', -30),
            'Light Saber' : ('a Light Saber', -40),
            'Infinity Gauntlet' : ('the Infinity Gauntlet', -100)
        }
        self.weapon_chosen = self.user_chooses_weapon_for_robot()
        self.robo_weapon = Weapon(self.weapon_chosen[0], self.weapon_chosen[1])

#Allows the user to select a permanent weapon for them to use throughout the match
    def user_chooses_weapon_for_robot(self):
        self.weapon_chosen = input(f"Let's get {self.robo_name} a weapon.\nYou have 5 choices plus one mystery choice.\nType 1 for 'Fly Swatter'.\nType 2 for 'Spatula'.\nType 3 for 'Battle Axe'.\nType 4 for 'Minigun'.\nType 5 for 'Light Saber'.\nType 6 for 'Mystery Weapon'.\nType your choice:  ")
        complete = False
        while complete == False:
            if self.weapon_chosen == '1':
                print(f'\n{self.robo_name} chooses a Fly Swatter?...ok.\n')
                return self.weapons_dict['Fly Swatter']
            elif self.weapon_chosen == '2':
                print(f'\n{self.robo_name} goes for the powerful Spatula!...wait..Spatula?\n')
                return self.weapons_dict['Spatula']
            elif self.weapon_chosen == '3':
                print(f'\n{self.robo_name} picks up a Battle Axe! Now we are talking.\n')
                return self.weapons_dict['Battle Axe']
            elif self.weapon_chosen == '4':
                print(f'\nMamacita bring out the Minigun for {self.robo_name}!\n')
                return (self.weapons_dict['Minigun'])
            elif self.weapon_chosen == '5':
                print(f'\nThe Light Saber, an elegant weapon from a more civilized age. Good choice {self.robo_name}.\n')
                return self.weapons_dict['Light Saber']
            elif self.weapon_chosen == '6':
                print(f"\n{self.robo_name} just borrowed Thanos's Infinity Gaunlet, be gentle on the poor fools.\n")
                return self.weapons_dict['Infinity Gauntlet']
            else:
                self.weapon_chosen = input("Sorry, you didn't input a valid command\nYou have 5 choices plus one mystery choice.\n To choose the 'Fly Swatter' Type 1:\nTo choose the 'Spatula' Type 2:\nTo choose the 'Battle Axe' Type 3:\nTo choose the 'Minigun' Type 4:\nTo choose the 'Light Saber' Type 5:\nTo choose the Mystery Weapon Type 6:  ")