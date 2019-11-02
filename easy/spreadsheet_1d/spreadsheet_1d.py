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
    def __init__(self, input_data):
        if not isinstance(input_data, list):
            input_data = [
                x for x in map(str.strip, input_data.split('\n')) if x]
        num_cells, formulas = int(input_data[0]), input_data[1:]
        self.cells = [Cell() for _ in range(num_cells)]
        self._apply_formulas(formulas)
        self._cursor = 0

    def _apply_formulas(self, formulas):
        for formulae, cell in zip(formulas, self.cells):
            cell.formulae = formulae

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor == len(self.cells):
            raise StopIteration
        else:
            self._cursor += 1
            return self._calculate_value(self._cursor-1)

    @cached
    def _calculate_value(self, cell_index):
        formulae = self.cells[cell_index].formulae
        operation, arg1, arg2 = self._parse_formulae(formulae)
        return operation.perform(arg1, arg2)

    def _parse_formulae(self, formulae):
        operation, arg1, arg2 = formulae.split()
        arg1, arg2 = map(self._parse_arg, (arg1, arg2))
        operation = Operations.__members__[operation].value
        return operation, arg1, arg2

    def _parse_arg(self, arg):
        m = re.search(r'\$(?P<cell_index>[0-9]+)', arg)
        if m:
            return self._calculate_value(int(m.group('cell_index')))
        return int(arg) if arg.lstrip('-').isdigit() else None


class Operation(ABC):
    @staticmethod
    @abstractmethod
    def perform(arg1, arg2):
        pass


class SetValue(Operation):
    @staticmethod
    def perform(arg1, arg2):
        return arg1


class Addition(Operation):
    @staticmethod
    def perform(arg1, arg2):
        return arg1 + arg2


class Subtraction(Operation):
    @staticmethod
    def perform(arg1, arg2):
        return arg1 - arg2


class Multiplication(Operation):
    @staticmethod
    def perform(arg1, arg2):
        return arg1 * arg2


class Operations(Enum):
    VALUE = SetValue
    ADD = Addition
    SUB = Subtraction
    MULT = Multiplication


if __name__ == '__main__':
    pass
