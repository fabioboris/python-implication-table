from state import State


class Cell:
    def __init__(self, row: State, column: State, eq: bool = False, not_eq: bool = False):
        self.row = row
        self.column = column
        self.eq = eq
        self.not_eq = not_eq
