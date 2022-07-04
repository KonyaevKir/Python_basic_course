from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload



class Plane(Vehicle):
    """
    создайте класс `Plane`, наследник `Vehicle`
    """
    cargo = 0
    max_cargo = 0

    def __init__(self,  weight,  fuel, fuel_consumption, max_cargo):
        super().__init__(weight,  fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        current = self.cargo + value
        if current > self.max_cargo:
            raise CargoOverload(f"There is Overload. Acceptable only {self.max_cargo}, you have {current}")
        else:
            self.cargo = current

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo


