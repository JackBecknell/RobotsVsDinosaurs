from robot import Robot
names_of_robots = ['The Terminator','Robo Cop','Optimus Prime']


class Fleet:
    def __init__(self):
        self.robots_in_fleet = [Robot('The Terminator'), Robot('Robo Cop'), Robot('Optimus Prime')]

    def create_fleet(self):
        return self.robots_in_fleet