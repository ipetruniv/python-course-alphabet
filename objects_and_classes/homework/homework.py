import uuid
from objects_and_classes.homework.constants import *

"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars _count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""

class Cesar:
    def __init__(self, name, garages = list([])):
        self.name = name
        self.garages = garages
        self.register_id = uuid.uuid4()
    def __repr__(self):
        return f"Cesar(name = {self.name}, garages = {self.garages})"

    def __str__(self):
        return f"The collector name: {self.name}, he(she) has {self.garages})"

    def hit_hat(self):
        return sum(garage.hit_hat() for garage in self.garages)


    def garages_count(self):
        return len(self.garages)

    def add_car(self, car, *args):
        if args:
            for arg in args:
                arg.add(car)
        else:
            freeg = {}
            for garage in self.garages:
                freeg[garage.name] = garage.freeplaces()
            garagename = max(freeg)
            for mygarage in self.garages:
                if mygarage.name == garagename:
                    mygarage.add(car)


    # <=
    def __le__(self, other):
        if float(self.hit_hat()) <= float(other.hit_hat()):
            return True
        else:
            return False

    # >=
    def __ge__(self, other):
        if float(self.hit_hat()) >= float(other.hit_hat()):
            return True
        else:
            return False

    # <
    def __lt__(self, other):
        if float(self.hit_hat()) < float(other.hit_hat()):
            return True
        else:
            return False

    def __gt__(self, other):
        if float(self.hit_hat()) > float(other.hit_hat()):
            return True
        else:
            return False

    # ==
    def __eq__(self, other):
        if float(self.hit_hat()) == float(other.hit_hat()):
            return True
        else:
            return False

    # !=
    def __ne__(self, other):
        if float(self.hit_hat()) != float(other.hit_hat()):
            return True
        else:
            return False

class Car:
    def __init__(self, name, price, type, producer, mileage):
        self.name = name
        self.price = float(price)
        self.type = type
        self.producer = producer
        self.number = uuid.uuid4()
        self.mileage = mileage

        if self.type not in CARS_TYPES:
            raise ValueError("Type must be one of:", CARS_TYPES)


        if self.producer not in CARS_PRODUCER:
            raise ValueError("Producer must be one of:", CARS_PRODUCER)

    def __str__(self):
        return (f"The car name: {self.name}, its price: {self.price}, producer: {self.producer}, number: {self.number},"
                f" mileage: {self.mileage}")
    def __repr__(self):
        return (f"car(name = {self.name}, price = {self.price}, producer = {self.producer}, number = {self.number},"
                f" mileage = {self.mileage})")
    def logs(self):
        return (f"Car name: {self.name}\nPrice: {self.price}\nProducer: {self.producer}\nNumber: {self.number}"
                f"\nMileage: {self.mileage}")
    def print(self):
        return (f"Car name: {self.name}, Price: {self.price}, Producer: {self.producer}, Number: {self.number}, "
                f" Mileage: {self.mileage}")

    def new_number(self):
        self.number = uuid.uuid4()
        return str(self)

    # <=
    def __le__(self, other):
        if float(self.price) <=  float(other.price):
            return True
        else:
            return False

    # >=
    def __ge__(self, other):
        if float(self.price) >= float(other.price):
            return True
        else:
            return False

    # <
    def __lt__(self, other):
        if float(self.price) < float(other.price):
            return True
        else:
            return False

    def __gt__(self, other):
        if float(self.price) > float(other.price):
            return True
        else:
            return False

    # ==
    def __eq__(self, other):
        if float(self.price) == float(other.price):
            return True
        else:
            return False

    # !=
    def __ne__(self, other):
        if float(self.price) != float(other.price):
            return True
        else:
            return False



class Garage:
    def __init__(self, name, town, cars: list, places: int):
        self.name = name
        self.town = town
        self.cars = cars
        self.owner = uuid.uuid4()
        self.places = places

        if self.town not in TOWNS:
            raise ValueError("The town must be one of:", TOWNS)


    def add(self, car):
        if len(self.cars) < self.places:
            self.cars.append(car)
            print(f"{car} added to garage {self.name}")
        else:
            return f"Garage is full"

    def remove(self, car):
        self.cars.remove(car)
        print(f"{car} removed from garage {self.name}")

    def hit_hat(self):
        return sum(carn.price for carn in self.cars)

    def car_list(self):
        for car in self.cars:
            print(str(car))

    def freeplaces(self):
        return self.places - len(self.cars)


# if __name__ == "__main__":
#
#
#     chery01 = Car("Tigo", 3000, "Wagon", "Chery", 3000)
#     ford01 = Car("Mustang", 4000, "Coupe", "Ford", 5000)
#     bugatti01 = Car("Chiron", 2000, "Van", "Bugatti", 5000)
#
#     garage1 = Garage("01_Garage", "Kiev",[chery01, ford01], 5)
#     #print(f"The summ of all cars in {garage1.name}  garage is: {garage1.hit_hat()}")
#     print("==" * 20)
#     garage1.add(bugatti01)
#     print(f"The summ of all cars in {garage1.name}  garage is: {garage1.hit_hat()}")
#     #print("==" * 20)
#
#     bugatti02 = Car("Divo", 8000, "Coupe", "Bugatti", 3000)
#     garage2 = Garage("02_Garage", "London", [bugatti02], 1)
#     print(f"The summ of all cars in {garage2.name}  garage is: {garage2.hit_hat()}")
#     #print("==" * 20)
#
#     chery03 = Car("Tigo", 5000, "Wagon", "Chery", 3000)
#     ford03 = Car("Mustang", 4000, "Coupe", "Ford", 5000)
#     bugatti03 = Car("Chiron", 1000, "Van", "Bugatti", 5000)
#     garage3 = Garage("03_Garage", "Amsterdam", [chery03, ford03, bugatti03], 5)
#     print(f"The summ of all cars in {garage3.name}  garage is: {garage3.hit_hat()}")
#     print("==" * 20)
#
#     chery05 = Car("Tigo", 2000, "Wagon", "Chery", 3000)
#     ford05 = Car("Mustang", 20000, "Coupe", "Ford", 5000)
#     bugatti05 = Car("Chiron", 400, "Van", "Bugatti", 5000)
#     garage5 = Garage("05_Garage", "Berlin", [chery05, ford05], 5)
#     print(f"The summ of all cars in {garage5.name}  garage is: {garage5.hit_hat()}")
#
#     colector01 = Cesar("Colector01",[garage1, garage2])
#     colector02 = Cesar("Colector01",[garage3, garage5])
#     print(f"Cesar01: all cars price {colector01.hit_hat()}, has {colector01.garages_count()} garages")
#     print(f"Cesar02: all cars price {colector02.hit_hat()}, has {colector02.garages_count()} garages")
#     print(garage1.car_list())
#     colector01.add_car(bugatti05,garage1)
#     colector02.add_car(bugatti05)
#     print(garage1.car_list())
#     print(colector01 > colector02)
#     print(colector01 < colector02)
#     print(colector01 = colector02)
#     #print(f"Cesar01: all cars price {colector01.hit_hat()}, has {colector01.garages_count()} garages")
#
