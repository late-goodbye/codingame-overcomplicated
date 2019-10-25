import re
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

    def apply_formulas(self, formulas):
        for formulae, cell in zip(formulas.split('\n'), self.cells):
            cell.formulae = formulae

    @cached
    def calculate_value(self, cell_index):

        formulae = self.cells[cell_index].formulae
        operation, arg1, arg2 = self.parse_formulae(formulae)

        return operation(arg1, arg2)

    def parse_formulae(self, formulae):
        operation, arg1, arg2 = formulae.split()
        arg1, arg2 = map(self.parse_arg, (arg1, arg2))
        operation = Operations.__members__[operation]
        return operation, arg1, arg2

    def parse_arg(self, arg):
        m = re.search(r'\$(?P<cell_index>[0-9]+)', arg)
        if m:
            return self.calculate_value(int(m.group('cell_index')))
        return int(arg) if arg.isdigit else None


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
    VALUE = SetValue
    ADD = Addition
    SUB = Subtraction
    MULT = Multiplication

if __name__ == '__main__':
    pass