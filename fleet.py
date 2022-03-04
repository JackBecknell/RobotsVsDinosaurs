from robot import Robot

class Fleet:
    def __init__(self):
        self.robots_in_fleet = [Robot('The Terminator'), Robot('Robo Cop'), Robot('Optimus Prime')]

    def create_fleet(self):
        return self.robots_in_fleet