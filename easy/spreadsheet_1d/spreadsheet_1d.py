import re
from abc import ABC, abstractmethod
from enum import Enum


class Cell(object):

    def __init__(self, spreadsheet):
        self.formulae = None
        self.calculated_value = None
        self.spreadsheet = spreadsheet

    @property
    def value(self):
        return self.calculated_value or self.calculate_value()

    def calculate_value(self):
        op, arg1, arg2 = map(self.resolve, self.formulae.split())
        return op.perform(arg1, arg2)

    def resolve(self, param):
        return self.resolve_operator(param) or self.resolve_arg(param) or None

    def resolve_arg(self, arg):
        m = re.search(r'\$(?P<index>[0-9]+)', arg)
        if m:
            return self.spreadsheet.get_cell(int(m.group('index'))).value
        elif arg.isdigit():
            return int(arg)

    @staticmethod
    def resolve_operator(operator):
        return Operations.get[operator].value or None


class Spreadsheet(object):

    def __init__(self, num_cells):
        self.cells = [Cell(self) for _ in num_cells]
        self.cursor = 0

    def get_cell(self, index):
        return self.cells[index]

    def set_formulae(self, formulae, cursor=None):
        cursor = cursor or self.cursor
        self.get_cell(cursor).formulae = formulae

    def calculate_cells(self):
        #TODO finish later
        pass

class Operation(ABC):

    @classmethod
    @abstractmethod
    def perform(cls, arg1: int, arg2: int):
        pass


class SetValue(Operation):

    @classmethod
    def perform(cls, arg1: int, arg2: int):
        return arg1


class Addition(Operation):

    @classmethod
    def perform(cls, arg1: int, arg2: int):
        return arg1 + arg2


class Subtraction(Operation):

    @classmethod
    def perform(cls, arg1: int, arg2: int):
        return arg1 - arg2


class Multiplication(Operation):

    @classmethod
    def perform(cls, arg1: int, arg2: int):
        return arg1 * arg2


class Operations(Enum):
    VALUE = SetValue
    ADD = Addition
    SUB = Subtraction
    MULT = Multiplication
