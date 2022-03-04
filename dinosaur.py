#FOR BONUS 2. This will be used to let the user choose an attack for their dinosaur to use.
dinosaur_attack_choices = [('Ad hominem', -1), ('Dino-sit', -10), ('Stomp', -15), ('Slash', -20), ('Bite', -25), ('Let Godzilla work!', -100)]


class Dinosaur:
    def __init__(self, pass_name):
        self.dino_name = pass_name
        self.dino_attack_power = self.user_chooses_current_dino_attack()
        self.dino_health = 100
        self.dino_energy_level = 100

    def dino_attack(self, pass_robot_to_be_attacked):
        pass

    def user_chooses_current_dino_attack(self):
        self.attack_chosen = input(f"Alright gamer, what attack do you want {self.dino_name} to use next?\nType 1 for 'Ad hominem'.\nType 2 for 'Dino-sit'.\nType 3 for 'Stomp'.\nType 4 for 'Slash'.\nType 5 for 'Bite'.\nType 6 for 'Mystery attack'.\n")
        complete = False
        while complete == False:
            if self.attack_chosen == '1':
                print('Ah yes, Ad hominem, some wounds never heal')
                self.attack_chosen = dinosaur_attack_choices[0]
                return self.attack_chosen
            elif self.attack_chosen == '2':
                print('Dino-sit, more humiliating than anything.')
                self.attack_chosen = dinosaur_attack_choices[1]
                return self.attack_chosen
            elif self.attack_chosen == '3':
                print("Left foot, let's Stomp! Cha-cha now yall! Criss-Cross!!!")
                self.attack_chosen = dinosaur_attack_choices[2]
                return self.attack_chosen
            elif self.attack_chosen == '4':
                print("Slash and watch em bleed..or leak.")
                self.attack_chosen = dinosaur_attack_choices[3]
                return self.attack_chosen
            elif self.attack_chosen == '5':
                print("Bite! It is recomended you see a dentist after this.")
                self.attack_chosen = dinosaur_attack_choices[4]
                return self.attack_chosen
            elif self.attack_chosen == '6':
                print(f"Instead of sending {self.dino_name} to fight you ask GodZilla for a hand, it's VERY effective")
                self.attack_chosen = dinosaur_attack_choices[5]
                return self.attack_chosen
            else:
                self.attack_chosen = input("Sorry kiddo, That wasn't a proper command.\n What attack do you want next?\nType 1 for 'Ad hominem'.\nType 2 for 'Dino-sit'.\nType 3 for 'Stomp'.\nType 4 for 'Slash'.\nType 5 for 'Bite'.\nType 6 for 'Ask GodZilla for a hand'.\n")