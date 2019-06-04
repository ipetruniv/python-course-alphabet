from __future__ import annotations
import uuid
import random
import pickle
from objects_and_classes.homework.constants import *
import json

class Cesar:
    def __init__(self, name, *args):
        self.name = name
        if args:
            for arg in args:
                if type(arg) == Car:
                    self.garages.append(arg)
                else:
                    raise TypeError("Object is not a Car")
        else:
            self.garages = []
        self.register_id = uuid.uuid4()

    def __repr__(self):
        return f"Cesar(name = {self.name}, garages = {self.garages})"

    def __str__(self):
        return f"{self.name}"

    def __setstate__(self, state):
        self.__dict__ = state

    def __getstate__(self):
        return self.__dict__.copy()

    def hit_car(self):
        return sum(_.hit_car() for _ in self.garages)

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        cars_c = 0
        for g in self.garages:
            cars_c += len(g.cars)

        return cars_c

    def add_car(self, car, *args):
        if args:
            for arg in args:
                arg.add(car)
        else:
            freeg = {}
            for ng in self.garages:
                freeg[ng] = ng.freeplaces()
            garagename = max(freeg)
            for mygarage in self.garages:
                if mygarage.name == garagename:
                    mygarage.add(car)

    def add_garage(self, new_garage):
        new_garage.owner = self.register_id
        self.garages.append(new_garage)


    # <=
    def __le__(self, other):
        return float(self.hit_car()) <= float(other.hit_car())

    # >=
    def __ge__(self, other):
        return float(self.hit_car()) >= float(other.hit_car())

    # <
    def __lt__(self, other):
        return float(self.hit_car()) < float(other.hit_car())

    def __gt__(self, other):
        return float(self.hit_car()) > float(other.hit_car())

    # ==
    def __eq__(self, other):
        return float(self.hit_car()) == float(other.hit_car())

    # !=
    def __ne__(self, other):
        return float(self.hit_car()) != float(other.hit_car())

    # # Serialization HW
    # @staticmethod
    # def to_json(obj):
    #     return json.dumps(Car.print(obj))
    #
    #
    # @classmethod
    # def from_json(cls, data):
    #     car_data = json.loads(data)
    #     return Car(car_data["price"],
    #                car_data["type"],
    #                car_data["producer"],
    #                car_data["mileage"],
    #                car_data["number"])

if __name__ == "__main__":
    # Generate the owners (Cesars):
    cesars = [Cesar(cesar) for cesar in ["Ihor", "Denis", "Olga", "Vika"]]
    for cesar in cesars:
        print(f"Obj type: {type(cesar)}, Obj {str(cesar)}")