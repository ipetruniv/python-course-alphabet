from objects_and_classes.homework.constants import *
from __future__ import annotations
import uuid


"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.
"""
#
# class Cesar:
#     """
#     Колекціонер має наступні характеристики
#     name - значення типу str. Його ім'я
#     garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
#     register_id - UUID; Унікальна айдішка Колекціонера.
#
#     Повинні бути реалізовані наступні методи:
#     hit_hat() - повертає ціну всіх його автомобілів.
#     garages_count() - вертає кількість гаріжів.
#     сars_count() - вертає кількість машиню
#     add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
#     Якщо вільних місць немає повинне вивести повідомлення про це.
#
#     Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
#     """
#     pass


class Car:
    """
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
    """
    def __init__(self, price: float, cartype: stt, produces: str, mileage: float, number ):
        self.price = price
        self.type = type
        if self.type in CARS_TYPES:
                self.cartype = cartype
        else:
            print("Car type must be in one of:)"
            for car_type in CARS_TYPES:
                print(car_type)

        if producer in CARS_PRODUCER:
                self.produces = producer
        else:
            print("Car producer must be one of:)"
            for producer in CARS_PRODUCER:
                print(producer)
        if number:
            self.number = number
        else:
            self.number = uuid.uuid1()

        self.mileage = mileage

    def __str__(self):
        return f"Car: price: {self.price} type: {self.cartype} producer: {self.produces} mileage: {self.mileage} " \
            f"number: {self.number}"

    def __repr__(self):
        return f"{self.__module__}.{type(self)} object at {hex(id(self))}>"


#
# class Garage:
#     """Гараж має наступні характеристики:
#
#     town - одне з перечислениз значеннь в TOWNS
#     cars - список з усіх автомобілів які знаходяться в гаражі
#     places - значення типу int. Максимально допустима кількість автомобілів в гаражі
#     owner - значення типу UUID. За дефолтом None.
#
#
#     Повинен мати реалізованими наступні методи
#
#     add(car) -> Добавляє машину в гараж, якщо є вільні місця
#     remove(cat) -> Забирає машину з гаражу.
#     hit_hat() -> Вертає сумарну вартість всіх машин в гаражі
# """
#
#     def __init__(self, name, town, cars, places, owner = None) -> None:
#         # print("Fill out programmer with attributes")
#         self.name = name
#         self.town = town
#         self.cars = cars
#         self.places = places
#         self.owner = owner
#
#
#     def __add__(self):
#         pass
#
#
#     def __remove__(self):
#         pass
#
#
#     def __hit_car__(self):
#         pass

#print(CARS_TYPES)
#print(type(CARS_TYPES))
#my_car01 = Car(500, 'Sedan', 'BMW', 500)
#print(mycar01)

