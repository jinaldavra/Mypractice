from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine():
        pass

class Bike(Vehicle):
    def start_engine(self):
        return "Start with a key or kick."
    
class Car(Vehicle):
    def start_engine(self):
        return "Start with a key."
    
class Bus(Vehicle):
    def start_engine(self):
        return "Start with a key."
    
obj_of_bike = Bike()
# print(obj_of_bike.start_engine())

obj_of_car = Car()
# print(obj_of_car.start_engine())

obj_of_bus = Bus()
print(obj_of_bus.start_engine())
