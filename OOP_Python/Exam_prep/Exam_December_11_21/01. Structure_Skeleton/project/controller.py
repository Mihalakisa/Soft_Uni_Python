from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in ['MuscleCar', 'SportsCar']:
            return
        if model in [car.model for car in self.cars]:
            raise Exception(f"Car {model} is already created!")

        new_car = None
        if car_type == 'MuscleCar':
            new_car = MuscleCar(model, speed_limit)
        elif car_type == 'SportsCar':
            new_car = SportsCar(model, speed_limit)

        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {new_driver.name} is created."

    def create_race(self, race_name: str):
        if any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race.name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_car(car_type)

        return driver.change_car(car)

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race(race_name)
        driver = self.__find_driver(driver_name)

        return race.register_driver(driver)

    def start_race(self, race_name: str):
        race = self.__find_race(race_name)

        return race.start()

    def __find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def __find_car(self, car_type):
        for idx in range(len(self.cars)-1, -1, -1):
            car = self.cars[idx]

            if not car.is_taken and car.__class__.__name__ == car_type:
                return car
        raise Exception(f"Car {car_type} could not be found!")

    def __find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")
