from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


class Vehicle(ABC):
    def __init__(self, make, model, spec) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    spec = "US Spec"

    def create_car(self, make, model) -> Vehicle:
        return Car(make, model, self.spec)

    def create_motorcycle(self, make, model) -> Vehicle:
        return Motorcycle(make, model, self.spec)


class EUVehicleFactory(VehicleFactory):
    spec = "EU Spec"

    def create_car(self, make, model) -> Vehicle:
        return Car(make, model, self.spec)

    def create_motorcycle(self, make, model) -> Vehicle:
        return Motorcycle(make, model, self.spec)


def main():
    us_factory = USVehicleFactory()
    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    eu_factory = EUVehicleFactory()
    vehicle2 = eu_factory.create_car("BMW", "M6")
    vehicle2.start_engine()

    vehicle3 = eu_factory.create_motorcycle("Riga", "v1")
    vehicle3.start_engine()


if __name__ == "__main__":
    main()
