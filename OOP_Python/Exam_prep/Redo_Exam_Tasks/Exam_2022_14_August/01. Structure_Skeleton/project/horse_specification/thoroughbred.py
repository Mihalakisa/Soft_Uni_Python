from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def max_horse_speed(self):
        return 140

    def train(self):
        if self.speed <= 137:
            self.speed += 3
        elif self.speed < 140:
            self.speed = 140
