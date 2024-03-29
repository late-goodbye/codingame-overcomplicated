# Statement

You are given a 1-dimensional spreadsheet. You are to resolve the formulae
and give the value of all its cells.

Each input cell's content is peovided as an _operation_ with two operands
_arg1_ and _arg2_.

There are 4 types of operations:

**VALUE** _arg1_ _arg2_: The cell's value is _arg1_, (_arg2_ is not used
and will be "_" to aid parsing).

**ADD** _arg1_ _arg2_: The cell's value is _arg1_ + _arg2_.

**SUB** _arg1_ _arg2_: The cell's value is _arg1_ - _arg2_.

**MULT** _arg1_ _arg2_: The cell's value is _arg1_ x _arg2_.

Arguments can be of two types:

* **Reference** _$ref_: If an argument starts with a dollar sign, it is
a interpreted as a reference and its value is equal to the value of the
cell by that number _ref_, 0-indexed.
For example, "$0" will have the value of result of the first cell.
Note that a cell can reference a cell after itself!

* **Value** _val_: If an argument is a pure number, its value is _val_.
For example, "3" will have the value 3.

There won't be any cyclic references: a cell that reference itself
or a cell that references it, directly or indirectly.

## Input

**Line 1:** An integer _N_ for the number of cells.

**Next _N_ lines:** _operation_ _arg1_ _arg2_

_operation_ is one of { **VALUE**, **ADD**, **SUB**, **MULT** }

_arg1_ and _arg2_ are either a number ("-?[0-9]+"),
a reference ("\$[0-9]+") or nothing "_".

## Output

**_N_ lines:** the value of each cell, one value per line,
from cell 0 to _N_.

## Constraints

1 <= **N** <= 100

-10000 <= **val** <= 10000

$0 <= $**ref** <= $(**N** - 1)

**val** in Z

**ref** in N

There are **no** cyclic references.

## Example

### Input

2

VALUE 3 _

ADD $0 4

### Output

3

7