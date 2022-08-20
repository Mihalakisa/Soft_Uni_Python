from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def max_horse_speed(self):
        return 120

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        elif self.speed < 120:
            self.speed = 120
