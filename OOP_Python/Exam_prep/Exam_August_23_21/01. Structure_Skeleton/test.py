from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.space_station import SpaceStation

space_station = SpaceStation()

# print(space_station.add_planet('Mars', 'Item1'))
# print(space_station.add_planet('Mars', 'Item1'))
# print(space_station.add_astronaut('Biologist', 'Pesho'))
# print(space_station.retire_astronaut('Pesho'))

astronauts = [
    Biologist('Name1'),
    Biologist('Name2'),
    Meteorologist('Name3'),
    Geodesist('Name4'),
    Geodesist('Name5'),
    Meteorologist('Name6'),
    Biologist('Name7')
]

