from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    STARTING_WEIGHT = 7

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, self.STARTING_WEIGHT)

    def eating(self):
        self.STARTING_WEIGHT += 1
