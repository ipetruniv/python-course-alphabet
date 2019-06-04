import sys
import os
import uuid
import random
import json
import pickle
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from objects_and_classes.homework.constants import *
import glob

class Car:
    def __init__(self, price, type, producer, mileage, number = None):
        self.price = float(price)
        self.type = type
        self.producer = producer
        if number == None:
            self.number = uuid.uuid4()
        else:
            self.number = uuid.UUID(number)
        self.mileage = mileage

        if self.type not in CARS_TYPES:
            raise ValueError("Type must be one of:", CARS_TYPES)

        if self.producer not in CARS_PRODUCER:
            raise ValueError("Producer must be one of:", CARS_PRODUCER)

    def __setstate__(self, state):
        self.__dict__ = state

    def __getstate__(self):
        return self.__dict__

    def __str__(self):
        return (f"Price: {self.price}, Producer: {self.producer}, Number: {self.number},"
                f" mileage: {self.mileage}")

    def __repr__(self):
        return (f"car(price = {self.price}, producer = {self.producer}, number = {self.number},"
                f" mileage = {self.mileage})")

    def logs(self):
        return str(self)

    def print(self):
        data = {"price": self.price,
                "type": self.type,
                "producer": self.producer,
                "number": str(self.number),
                "mileage": self.mileage}
        return data

    def new_number(self):
        self.number = uuid.uuid4()
        return str(self)

    # <=
    def __le__(self, other):
        return float(self.price) <=  float(other.price)

    # >=
    def __ge__(self, other):
        return float(self.price) >= float(other.price)

    # <
    def __lt__(self, other):
        return float(self.price) < float(other.price)

    def __gt__(self, other):
        return float(self.price) > float(other.price)

    # ==
    def __eq__(self, other):
        return float(self.price) == float(other.price)

    # !=
    def __ne__(self, other):
        return float(self.price) != float(other.price)

    @staticmethod
    def to_json_str(obj):
        return json.dumps(Car.print(obj))

    @classmethod
    def from_json_str(cls, data):
        car_data = json.loads(data)
        return Car(car_data["price"],
                   car_data["type"],
                   car_data["producer"],
                   car_data["mileage"],
                   car_data["number"])

    @staticmethod
    def to_yaml(self):
        yaml = YAML()
        filename = 'Dump_' + str(self.number) + '.yaml'

        try:
            with open(filename, "w") as file:
                yaml.dump(Car.print(self), file)
            print("Saved")
        except Exception as e:
            print(e)

    @classmethod
    def from_yaml(cls, dump_file):
        yaml = YAML()
        with open(dump_file, "r") as file:
            car_conf = yaml.load(dump_file)
            print(f" price: {car_conf['price']}, type: {car_conf['type']}, producer: {car_conf['producer']},"
                f"mileage:{car_conf['mileage']}, number: {car_conf['number']}")
        # return Car(price = int(car_conf['price']),
        #            type = car_conf['type'],
        #            producer = car_conf['producer'],
        #            mileage = car_conf['mileage'],
        #            number = car_conf['number'])

if __name__ == "__main__":
    def separator():
        print(f"{'==' * 30}")

    def generate_cars():
        # Generate cars
        cars = []
        for car_counts in range(random.randint(5, 10)):
            new_car = Car(
                price = random.randint(3000, 50000),
                type = random.choice(CARS_TYPES),
                producer = random.choice(CARS_PRODUCER),
                mileage = random.randint(5000, 100000)
            )
            cars.append(new_car)
        return cars

    def compare_cars(cars):
        for _ in range(0, len(cars) - 1):
            print(f"First car {cars[_]}")
            print(f"Second car {cars[_ + 1]}")
            print(f" 1 > 2 : {cars[_] > cars[_ + 1]}")
            print(f" 1 >= 2 : {cars[_] >= cars[_ + 1]}")
            print(f" 1 < 2 : {cars[_] < cars[_ + 1]}")
            print(f" 1 <= 2 : {cars[_] <= cars[_ + 1]}")
            print(f" 1 == 2 : {cars[_] == cars[_ + 1]}")
            print(f" 1 != 2 : {cars[_] != cars[_ + 1]}")

    def export_import_to_json_str(cars):
        for car in cars:
            json_car = car.to_json_str(car)
            print('==' * 30)
            print(f"The Json string: {json_car}")
            car_from_json = car.from_json_str(json_car)
            print(f"The original object:")
            print(f"Object type: {type(car)}\n Object data: {car}")
            print(f"The new object:")
            print(f"Object type: {type(car_from_json)}\n Object data: {car_from_json}")

    def dump_to_yaml(cars):
        for car in cars:
            car.to_yaml(car)

    def restore_fron_yaml():
        cars = []
        curr_path = os.path.dirname(os.path.realpath(__file__))
        dummps = curr_path + '\\Dump_*.yaml'
        files = glob.glob(dummps)
        for file in files:
            car = Car.from_yaml(file)
            cars.append(car)
            print(car)



    # cars = generate_cars()
    # dump_to_yaml(cars)
    restore_fron_yaml()

