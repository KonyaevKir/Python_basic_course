from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    weight = 0
    fuel = 0
    fuel_consumption = 0
    started = False

    def __init__(self, weight = 0,  fuel = 0, fuel_consumption = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started and self.fuel <= 0:
            raise LowFuelError("There is no petrol in the tank")
        else:
            self.started = True

    def move(self, distance):
        allow_dist = self.fuel/(self.fuel_consumption)
        if allow_dist < distance:
            raise NotEnoughFuel(f"Not enough fuel to {distance} just for {allow_dist}")
        else:
            self.fuel = self.fuel - self.fuel_consumption * distance
