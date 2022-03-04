from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.opening_message()
        self.dinosaurs_in_herd = [Dinosaur('T-rex'), Dinosaur('Velociraptor'), Dinosaur('Spinosaurus')]

    def create_herd(self):
        return self.dinosaurs_in_herd

    def opening_message(self):
        print("Next, let's select what attacks each of our dinosaurs will use when it is their turn.")