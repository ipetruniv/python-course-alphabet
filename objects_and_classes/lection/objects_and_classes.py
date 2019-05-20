import typing

# This is object of class
# There is only one object of the same class.
from utils import describe_object
import time

class Student:
    def __init__(self, name = "Anton"):
        # print(f"Called the method init")
        # print(f" Name: {name}")
        self.name = name
        # print(f"Self name: {self.name} Name: {name}")
        # print(f"Self name ID: {id(self.name)} Name Id: {id(name)}")
        self.enought_coffee = False

    def __new__(cls, *args, **kwargs):
        """
        This methods calls when object is created.
        When new instance if class is created this method is called and return instance

        Returns:
            instance of class
        """

        # print("We create new object that will be map as programmer")
        #print("We create new object that wprint(f" Called the method new {obj} ")ill be map as programmer")
        obj = super(Student, cls).__new__(cls)
        # print(f"Called the method new {obj} the object id is {id(obj)}")
        return obj

    def __del__(self):
        #print(f"The object {id(self)} deleted")
        pass

    def __enter__(self):
        self.enought_coffee = True
        # print(f"This is enter block {id(self)}")
        # return "This is return from enter"


    def __exit__(self, type, value, traceback):
        self.enought_coffee = False
        # print(f"This is exit block {id(self)}")

    def work(self):
        if self.enought_coffee:
            print(f"{self.name} need some coffee WORK function coffee is {self.enought_coffee}")
            return

        for k in range(10):
            time.sleep(2)
            print(f"{self.name} is WORK function for block coffee is {self.enought_coffee}")


    def __str__(self):
        return f"Name: {self.name} Need coffee: {self.enought_coffee}"

    def __repr__(self):
        return f"Student(\"name = {self.name}\")"




# print(describe_object(name="Student", obj=Student))
# This is instances of class Student

# It could be a lot of instances of one class
# student_1 = Student()
# print("==" * 50)
# print(f"Return student name: {student_1.name} It's ID: {id(student_1)}")
# print("==" * 80)
student_1 = Student("Ihor")
# print("==" * 50)
# print(f"Return student name: {student_1.name} student ID: {id(student_1)}")

# print("==" * 80)
#
#
# print(f"this is main app before with the coffee is {student_1.enought_coffee}")
# print("==" * 30)
# with student_1 as p:
#     print("==" * 30)
#     print(f"this is WITH coffee is {student_1.enought_coffee}")
#     print("==" * 30)
#     student_1.enought_coffee = False
#     student_1.work()

# print("==" * 30)
# print(f"The exit should be in previos line coffee is {student_1.enought_coffee}")
# student_2 = Student()
# student_3 = Student()

# print(describe_object("student_1", student_1))
# print(describe_object("student_2", student_2))
# print(describe_object("student_3", student_3))


# some_int = 10
# print(dir(some_int))
# print(str(student_1))
# print(repr(student_1))

res = repr(student_1)
print(res)
student_2 = eval(res)
print("Student 2: ", student_2)