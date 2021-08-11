from state import State


class Cell:
    def __init__(self, left: State, right: State, eq: bool = False, not_eq: bool = False):
        self.left = left
        self.right = right
        self.eq = eq
        self.not_eq = not_eq
