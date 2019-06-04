import uuid
import random
import json
import pickle
from objects_and_classes.homework.constants import *

class Garage:
    def __init__(self, town, places: int, cars = []):
        self.town = town
        self.cars = cars
        self.owner = None
        self.places = places

        if self.town not in TOWNS:
            raise ValueError("The town must be one of:", TOWNS)

    def __repr__(self):
        return f"town = {self.town}, cars = {self.cars}, places = {self.places}"

    def __setstate__(self, state):
        self.__dict__ = state

    def __getstate__(self):
        return self.__dict__

    @classmethod
    def from_json(cls, data):
        town = data.get('town')
        cars = data.get('cars')
        places = data.get('places')
        new_garage = Garage(town = town, places = places)
        return new_garage

    @staticmethod
    def to_json(obj: Garage):
        data = {"town": obj.town,
                "cars": obj.cars,
                "places": obj.places,
                "owner": obj.owner
                }
        return data

    def add(self, car):
        if len(self.cars) < self.places:
            self.cars.append(car)
        else:
            raise OverflowError("Garage is full")

    def remove(self, car):
        try:
            self.cars.remove(car)
        except:
            raise Exception("Car not found")

    def hit_car(self):
        return sum(carn.price for carn in self.cars)

    def car_list(self):
        for car in self.cars:
            print(str(car))

    def free_places(self):
        return self.places - len(self.cars)


