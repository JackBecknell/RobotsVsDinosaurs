from dinosaur import Dinosaur
dinosaur_1 = Dinosaur('T-rex')
dinosaur_2 = Dinosaur('Velociraptor')
dinosaur_3 = Dinosaur('Spinosaurus')
class Herd:
    def __init__(self):
        self.dinosaurs_in_herd = [dinosaur_1, dinosaur_2, dinosaur_3]

    def create_herd(self):
        return self.dinosaurs_in_herd