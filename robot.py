from weapon import Weapon

#FOR BONUS 1. This will be used to let the user choose a weapon for each robot that will then be assigned as it's own.
#Find a better way, make the list below and instance method.
robot_weapon_choices = [('Fly Swatter', -1), ('Spatula', -10), ('Battle Axe', -15),('Minigun', -20), ('Light Saber', -25), ('Infinity Gaunlet', -100)]


class Robot:
    def __init__(self, pass_name):
        self.robo_name = pass_name
        self.robo_health = 100
        self.robo_energy_level = 100
        self.weapon_chosen = self.user_chooses_weapon_for_robot()
        self.robo_weapon = Weapon(self.weapon_chosen[0], self.weapon_chosen[1])
    
    def robo_attack(self, pass_dinosaur_to_be_attacked):
        pass

    def user_chooses_weapon_for_robot(self):
        self.weapon_chosen = input(f"Let's get {self.robo_name} a weapon.\nYou have 5 choices plus one mystery choice.\nTo choose the 'Fly Swatter' Type 1:\nTo choose the 'Spatula' Type 2:\nTo choose the 'Battle Axe' Type 3:\nTo choose the 'Minigun' Type 4:\nTo choose the 'Light Saber' Type 5:\nTo choose the Mystery Weapon Type 6:\nType your choice:  ")
        complete = False
        while complete == False:
            if self.weapon_chosen == '1':
                print('Fly Swatter?...ok')
                return robot_weapon_choices[0]
            elif self.weapon_chosen == '2':
                print('The powerful Spatula!...wait..Spatula?')
                return robot_weapon_choices[1]
            elif self.weapon_chosen == '3':
                print('Battle Axe! Now we are talking.')
                return robot_weapon_choices[2]
            elif self.weapon_chosen == '4':
                print('Mamacita bring out the Minigun!')
                return robot_weapon_choices[3]
            elif self.weapon_chosen == '5':
                print('The Light Saber, an elegant weapon from a more civilized age.')
                return robot_weapon_choices[4]
            elif self.weapon_chosen == '6':
                print("You just borrowed Thanos's Infinity Gaunlet, be gentle on the poor fools.")
                return robot_weapon_choices[5]
            else:
                self.weapon_chosen = input("Sorry, you didn't input a valid command\nYou have 5 choices plus one mystery choice.\n To choose the 'Fly Swatter' Type 1:\nTo choose the 'Spatula' Type 2:\nTo choose the 'Battle Axe' Type 3:\nTo choose the 'Minigun' Type 4:\nTo choose the 'Light Saber' Type 5:\nTo choose the Mystery Weapon Type 6:  ")
