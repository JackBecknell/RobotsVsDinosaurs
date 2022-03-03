#FOR BONUS 2. This will be used to let the user choose an attack for their dinosaur to use.
dinosaur_attack_choices = [('Ad hominem', -1), ('Dino-sit', -10), ('Stomp', -15), ('Slash', -20), ('Bite', -25), ('a', -100)]

def user_chooses_current_dino_attack():
    attack_chosen = input("Alright gamer, what attack do you want next?\nType 1 for 'Ad hominem'.\nType 2 for 'Dino-sit'.\nType 3 for 'Stomp'.\nType 4 for 'Slash'.\nType 5 for 'Bite'.\nType 6 for 'Ask GodZilla for a hand'.\n")
    complete = False
    while complete == False:
        if attack_chosen == '1':
            print('Ah yes, Ad hominem, some wounds never heal')
            return attack_chosen
        elif attack_chosen == '2':
            print('Dino-sit, more humiliating than anything.')
            return attack_chosen
        elif attack_chosen == '3':
            print("Left foot, let's Stomp! Cha-cha now yall! Criss-Cross!!!")
            return attack_chosen
        elif attack_chosen == '4':
            print("Slash and watch em bleed..or leak.")
            return attack_chosen
        elif attack_chosen == '5':
            print("Bite! It is recomended you see a dentist after this.")
            return attack_chosen
        elif attack_chosen == '6':
            print("Instead of fighting yourself you ask GodZilla for a hand, it's VERY effective")
            return attack_chosen
        else:
            attack_chosen = input("Sorry kiddo, That wasn't a proper command.\n What attack do you want next?\nType 1 for 'Ad hominem'.\nType 2 for 'Dino-sit'.\nType 3 for 'Stomp'.\nType 4 for 'Slash'.\nType 5 for 'Bite'.\nType 6 for 'Ask GodZilla for a hand'.\n")

class Dinosaur:
    def __init__(self, pass_name):
        self.dino_name = pass_name
        self.dino_attack_power = user_chooses_current_dino_attack()
        self.dino_health = 100
        self.dino_energy_level = 100

    def dino_attack(self, pass_robot_to_be_attacked):
        pass