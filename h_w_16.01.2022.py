from abc import ABC, abstractmethod
import math

"""Создание абстрактного класса"""


class Root(ABC):
    def __init__(self, val_1, val_2):
        self.val_1 = val_1
        self.val_2 = val_2

    def calculate_linear_equation(self):
        root = -self.val_2 / self.val_1
        return root

    def quad_equation(self):
        disc = self.val_2 * 2 + 4 * self.val_1 * 3
        root_1 = (self.val_2 + math.sqrt(disc)) / (2 * self.val_1)
        root_2 = (self.val_2 - math.sqrt(disc)) / (2 * self.val_1)
        return root_1, root_2

    @abstractmethod
    def print_info(self):
        raise NotImplementedError


class Linear(Root):
    def __init__(self, val_1, val_2):
        super().__init__(val_1, val_2)

    def print_info(self):
        print(f"The root of {self.val_1}x+{self.val_2}=0 is: {round(self.calculate_linear_equation(), 2)}")


class Quad(Root):
    def __init__(self, val_1, val_2):
        super().__init__(val_1, val_2)

    def print_info(self):
        print(f"The roots of {self.val_1}x^2-{self.val_2}x-3=0 are: {self.quad_equation()}")


l = Linear(3, 7)
l.print_info()

w = Quad(1, 2)
w.print_info()
