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

    # Serialization HW
    @classmethod
    def import_from_file(filename: str, filetype: str):
        """
        filename - the name of file uses to import from
        filetype - the type of stored data syntax (one of yaml, json, pickle)
        """
        if filetype == 'yaml':
            pass

        if filetype == 'json':
            pass

        if filetype == 'pickle':
            with open(filename, "rb") as file:
                return pickle.load(file)



    def export_to_file(self, filename: str, filetype: str):
        """
        filename - the name of file uses for export to
        filetype - the type of stored data syntax (one of yaml, json, pickle)
        """
        if filetype == 'yaml':
            pass
        if filetype == 'json':
            pass

        if filetype == 'pickle':
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            return "Saved"

    def conver_to_str(self, strtype):
        """
        strtype  - the type of data syntax (one of yaml, json, pickle)
        """
        pass

    def create_from_str(self, strtype):
        """
        strtype  - the type of data syntax (one of yaml, json, pickle)
        """
        pass


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

    @classmethod
    def from_json(cls, data):
        price = data.get('price')
        type = data.get('type')
        producer = data.get('producer')
        number = data.get('number')
        mileage = data.get('mileage')
        new_car = Car(price = price, type = type, producer = producer, mileage = mileage, number = number  )
        return new_car

    @staticmethod
    def to_json(obj: Car):
        data = {"price": obj.price,
                "type": obj.type,
                "producer": obj.producer,
                "number": str(obj.number),
                "mileage": obj.mileage}
        return data

    def logs(self):
        return str(self)

    def print(self):
        return str(self)

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


if __name__ == "__main__":


    #Generate cars
    cars = []
    cars_json = []
    for car_counts in range(1, 5):
        new_car = Car(
            price = random.randint(3000, 50000),
            type = random.choice(CARS_TYPES),
            producer = random.choice(CARS_PRODUCER),
            mileage = random.randint(5000, 100000)
        )
        #print(new_car)
        print(new_car.to_json(new_car))
        cars_json.append(new_car.to_json(new_car))
        #cars.append(new_car)
        del new_car, car_counts
    print("Load from json")
    for car in cars_json:
        newcar = Car.from_json(car)
        print(newcar)



    #Generate garages
    garages_list = []
    garages_json = []
    for garage_count in range(1, 7):
        new_garage = Garage(random.choice(TOWNS),
                            random.randint(2,10))
        print(f" New Garage has been created: \n{str(new_garage)}")
        json_garage = Garage.to_json(new_garage)
        print(json_garage)
        garages_json.append(json_garage)
        #garages_list.append(new_garage)
        del new_garage, garage_count

    print(f"Garages from Json \n")
    for new_garage in garages_json:
        garage = Garage.from_json(new_garage)
        print(garage)
        garages_list.append(garage)



    #Move cars to garage
    for some_car in cars:
        choice_garage = random.choice(garages_list)
        if choice_garage.free_places() >= 1:
            choice_garage.add(some_car)


    #Generate the owners (Cesars):
    cesars = [Cesar(cesar) for cesar in ["Ihor", "Denis", "Olga", "Vika"]]

    # #Restore from pickle
    # cesars_names = ["Ihor", "Denis", "Olga", "Vika"]
    # cesars = []
    #
    # for cesar in cesars_names:
    #     filename = str(cesar) + '.pickle'
     #     with open(filename, "rb") as file:
    #          cesars.append(pickle.load(file))

    # #Assign garages to cesars (random)
    # for g in garages_list:
    #     curr_cesar = random.choice(cesars)
    #     curr_cesar.add_garage(g)
    #
    #
    #
    # print("The Colectors statistic")
    # for cesar in cesars:
    #     print(f"{'=' * 20} start for {str(cesar.name)} {'=' * 20}")
    #     print(f"Cear's {str(cesar.name)} garages list: {cesar.garages}")
    #     print(f"Cesar into Json \n")
    #     print(f"{'=' * 40}")
    #
    #     ##Dump to pickle
    #     # filename = str(cesar.name) + '.pickle'
    #     # with open(filename, "wb") as file:
    #     #     pickle.dump(cesar, file)
    #
    #     # json_formatted_str = json.dumps(cesar)
    #     # print(json_formatted_str)
    #
    #     for garage in cesar.garages:
    #         print(f"Cesar: {cesar.name} garage: {garage}")
    #         print(f"{'=' * 20} ")
    #         print(f"{str(cesar.name)} list of cars in {str(garage)}:")
    #         print(garage.car_list())
    #         print(f"{'=' * 20}")
    #         print(f"Ceasar: {cesar.name} {garage} all cars costs: {garage.hit_car()}")
    #
    #
    #     print(f"{str(cesar.name)}: has the {cesar.cars_count()} cars. The all cars price {cesar.hit_car()}, has {cesar.garages_count()} garages")
    #     print(f"{'====' * 20} end {'====' * 20} \n \n")
    #
    #
    #
