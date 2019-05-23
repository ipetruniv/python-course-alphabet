"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""
import uuid
import random
import json
import pickle
from objects_and_classes.homework.constants import *

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
    def __init__(self, price, type, producer, mileage):
        self.price = float(price)
        self.type = type
        self.producer = producer
        self.number = uuid.uuid4()
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
    def __init__(self, town, cars: list, places: int):
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
    for car_counts in range(random.randint(5, 10)):
        new_car = Car(
            price = random.randint(3000, 50000),
            type = random.choice(CARS_TYPES),
            producer = random.choice(CARS_PRODUCER),
            mileage = random.randint(5000, 100000)
        )
        cars.append(new_car)
        del new_car, car_counts

    #Generate garages
    garages_list = []
    for garage_count in range(1, random.randint(4, 7)):
        new_garage = Garage(random.choice(TOWNS),
                            [],
                            random.randint(2,10))
        #print(f" New Garage has been created: \n{str(new_garage)}")
        garages_list.append(new_garage)
        del new_garage, garage_count


    #Move cars to garage
    for some_car in cars:
        choice_garage = random.choice(garages_list)
        if choice_garage.free_places() >= 1:
            choice_garage.add(some_car)


    #Generate the owners (Cesars):
    cesars = [Cesar(cesar) for cesar in ["Ihor", "Denis", "Olga", "Vika"]]

    #Assign garages to cesars (random)
    for g in garages_list:
        curr_cesar = random.choice(cesars)
        curr_cesar.add_garage(g)



    print("The Colectors statistic")
    for cesar in cesars:
        print(f"{'=' * 20} start for {str(cesar.name)} {'=' * 20}")
        print(f"Cear's {str(cesar.name)} garages list: {cesar.garages}")
        for garage in cesar.garages:
            print(f"Cesar: {cesar.name} garage: {garage}")
            print(f"{'=' * 20} ")
            print(f"{str(cesar.name)} list of cars in {str(garage)}:")
            print(garage.car_list())
            print(f"{'=' * 20}")
            print(f"Ceasar: {cesar.name} {garage} all cars costs: {garage.hit_car()}")


        print(f"{str(cesar.name)}: has the {cesar.cars_count()} cars. The all cars price {cesar.hit_car()}, has {cesar.garages_count()} garages")
        print(f"{'====' * 20} end {'====' * 20} \n \n")



