from project.driver import Driver


class Race:

    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    def register_driver(self, driver: Driver):
        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

        if any(d.name == driver.name for d in self.drivers):
            raise Exception(f"Driver {driver.name} is already added in {self.name} race.")

        self.drivers.append(driver)
        return f"Driver {driver.name} added in {self.name} race."

    def start(self):
        if len(self.drivers) < 3:
            raise Exception(f"Race {self.name} cannot start with less than 3 participants!")
        winners = sorted(self.drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]

        result = ''
        for driver in winners:
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {self.name} race with a speed of {driver.car.speed_limit}.\n"
        return result.strip()
