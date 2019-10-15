from abc import abstractmethod, ABC
from enum import Enum
import re


class Cell(object):

    def __init__(self):
        self.value = 0


class Spreadsheet(object):

    def __init__(self, num_cells):
        self.cells = [Cell() for _ in range(num_cells)]
        self.cursor = 0

    def apply_formulae(self, formulae):
        op, arg1, arg2 = map(self.resolve, formulae.split())
        op.perform(arg1, arg2)

    def resolve_arg(self, arg):
        m = re.search(r'\$(?P<index>[0-9])+', arg)
        if m.group('index'):
            return self.cells[int(m.group('index'))]
        return int(arg)

    @staticmethod
    def resolve_operation(operation):
        if operation in Operations.__members__:
            return Operations[operation].value
        return None

    def resolve(self, attr):
        return self.resolve_operation(attr) or self.resolve_arg(attr)


class Operation(ABC):

    @classmethod
    @abstractmethod
    def perform(cls, cell: Cell, arg1: int, arg2: int):
        pass


class SetValue(Operation):

    @classmethod
    def perform(cls, cell: Cell, arg1: int, arg2: int):
        cell.value = arg1


class Addition(Operation):

    @classmethod
    def perform(cls, cell: Cell, arg1: int, arg2: int):
        cell.value = arg1 + arg2


class Subtraction(Operation):

    @classmethod
    def perform(cls, cell: Cell, arg1: int, arg2: int):
        cell.value = arg1 - arg2


class Multiplication(Operation):

    @classmethod
    def perform(cls, cell: Cell, arg1: int, arg2: int):
        cell.value = arg1 * arg2


class Operations(Enum):
    VALUE = SetValue
    ADD = Addition
    SUB = Subtraction
    MULT = Multiplication
