from robot import Robot
robot_1 = Robot('Robo 1')
robot_2 = Robot('Robo 2')
robot_3 = Robot('Robo 3')
class Fleet:
    def __init__(self):
        self.robots_in_fleet = [robot_1, robot_2, robot_3]

    def create_fleet(self):
        return self.robots_in_fleet