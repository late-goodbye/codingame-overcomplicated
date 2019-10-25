from abc import ABC, abstractmethod
from enum import Enum


def cached(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


class Cell:
    def __init__(self):
        self.formulae = None


class Spreadsheet:
    def __init__(self, num_cells):
        self.cells = [Cell() for _ in range(num_cells)]

    @cached
    def calculate_value(self, cell_index):

        formulae = self.cells[cell_index].formulae
        operation, arg1, arg2 = self.parse_formulae(formulae)

        return operation(arg1, arg2)


class Operation(ABC):
    @abstractmethod
    def perform(self, arg1, arg2):
        pass


class SetValue(Operation):
    def perform(self, arg1, arg2):
        return arg1


class Addition(Operation):
    def perform(self, arg1, arg2):
        return arg1 + arg2


class Subtraction(Operation):
    def perform(self, arg1, arg2):
        return arg1 - arg2


class Multiplication(Operation):
    def perform(self, arg1, arg2):
        return arg1 * arg2


class Operations(Enum):
    pass