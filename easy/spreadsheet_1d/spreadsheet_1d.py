from abc import ABC
from enum import Enum


class Cell(object):

    def __init__(self):
        self.formulae = None
        self.calculated_value = None

    @property
    def value(self):
        return self.calculated_value or self.calculate_value()

    def calculate_value(self):
        # TODO complete method
        op, arg1, arg2 = map(self.resolve, self.formulae.split())

    def resolve(self, param):
        return self.resolve_operator(param) or self.resolve_arg(param) or None

    @staticmethod
    def resolve_arg(arg):
        return int(arg) if arg.isdigit() else None

    @staticmethod
    def resolve_operator(operator):
        return Operators.get[operator].value or None


class Spreadsheet(object):
    pass


class Operator(ABC):
    pass


class Operators(Enum):
    VALUE = 1
    ADD = 2
    SUB = 3
    MULT = 4