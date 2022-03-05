def show_remaining_dino_options(self):
        self.dino_chosen = False
        while self.dino_chosen == False:
            if len(self.herd_on_battlefield.dinosaurs_in_herd) == 3:
                self.user_chooses_dino_for_turn = input(f"*************************************************************\n-Dino's Turn-\nWho Gets to Attack?\nEnter '1' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_energy_level}% energy level.\nEnter '2' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_energy_level}% energy level.\nEnter '3' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[2].dino_energy_level}% energy level.\n : ")
                if self.user_chooses_dino_for_turn in ['1','2' ,'3']:
                    self.dino_chosen = True
            elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 2:
                self.user_chooses_dino_for_turn = input(f"*************************************************************\n-Dino's Turn-\nBE CAREFUL! YOU'RE DOWN TO 2 DINOS!\nEnter '1' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_energy_level}% energy level.\nEnter '2' to attack with : {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_name} at {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_health} health, with {self.herd_on_battlefield.dinosaurs_in_herd[1].dino_energy_level}% energy level.\n : ")
                if self.user_chooses_dino_for_turn in ['1', '2']:
                    self.dino_chosen = True
            elif len(self.herd_on_battlefield.dinosaurs_in_herd) == 1:
                self.user_chooses_dino_for_turn = input(f"*************************************************************\n-Dino's Turn-\nThis is probably it...\nWell bud looks like your down to just {self.herd_on_battlefield.dinosaurs_in_herd[0].dino_name}. Press 1 followed by enter to make your last stand!\n : ")
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