from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self):
        self.wheels = 0

    @abstractmethod
    def turn(self):
        pass

    def print_wheel_count(self):
        print(self.__repr__() , ' has {} wheels.'.format(self.wheels))

    def __repr__(self):
        return str(self.__class__)


class Bike(Vehicle):
    def __init__(self, wheels):
        super().__init__()
        self.wheels = wheels

    def turn(self, direction):
        print('turning handle bar to ', direction)


o = Bike(2)
o.turn('right')
o.print_wheel_count()