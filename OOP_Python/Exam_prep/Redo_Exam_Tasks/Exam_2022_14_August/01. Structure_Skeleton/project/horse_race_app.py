from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ['Appaloosa', 'Thoroughbred']:
            return
        if any(horse.name for horse in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = None
        if horse_type == 'Appaloosa':
            new_horse = Appaloosa(horse_name, horse_speed)
        if horse_type == 'Thoroughbred':
            new_horse = Thoroughbred(horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(jockey.name for jockey in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        pass

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        pass

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        pass
