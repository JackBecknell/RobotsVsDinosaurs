from weapon import Weapon
class Robot:
    def __init__(self, pass_name):
        self.robo_name = pass_name
        self.robo_health = 100
        self.robo_weapon = Weapon()
    
    def robo_attack(self, pass_dinosaur_to_be_attacked):
        pass