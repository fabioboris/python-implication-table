from cell import Cell
from debug import DEBUG
from state import State
from type_aliases import ImplicationTable, InputMatrix, StatesTable


def create_states_table(input_matrix: InputMatrix) -> StatesTable:
    """Create the state objects list from the inputs table"""

    states = []

    for index, row in enumerate(input_matrix):
        _x0, _y0, _x1, _y1 = row
        states.append(State(index, _x0, _y0, _x1, _y1))

    return states


def create_implication_table(states) -> ImplicationTable:
    """Create the states table from the objects"""

    table = {}

    for i in range(len(states)):
        for j in range(i, len(states)):
            _key = i, j
            _eq = i == j
            table[_key] = Cell(states[i], states[j], _eq)

    return table


def search_non_eq_states(table: ImplicationTable):
    """Search for non equivalent cells"""

    if DEBUG:
        print("\n\nSearch for non equivalent cells:\n")

    for key, cell in table.items():
        if (cell.row.y0 != cell.column.y0 or cell.row.y1 != cell.column.y1):
            cell.not_eq = True

            if DEBUG and key[0] != key[1]:
                print(f"{key}: {cell.not_eq}")


def search_non_eq_next_states(table: ImplicationTable):
    """Search on vacant cells for non equivalent cell on next states"""

    if DEBUG:
        print("\n\nSearch on vacant cells for non equivalent cell on next states:")

    do_search = True
    while (do_search):
        if DEBUG:
            print("\nBegin iteration:")

        found = 0
        for key, cell in table.items():
            if not cell.eq and not cell.not_eq:
                _key1 = tuple(sorted((cell.row.x0, cell.column.x0)))
                _key2 = tuple(sorted((cell.row.x1, cell.column.x1)))

                if table[_key1].not_eq:
                    cell.not_eq = True
                    found += 1
                elif table[_key2].not_eq:
                    cell.not_eq = True
                    found += 1

                if DEBUG:
                    print(f"{key} -> {_key1}, {_key2}: {cell.not_eq}")

        if found == 0:
            do_search = False


def search_eq_states(table: ImplicationTable):
    """Mark vacant cells as equivalent"""

    if DEBUG:
        print("\n\nMark vacant cells as equivalent:\n")

    for key, cell in table.items():
        if not cell.eq and not cell.not_eq:
            cell.eq = True

            if DEBUG:
                print(f"{key}: {cell.eq}")


def remove_eq_states(table: ImplicationTable, states: StatesTable):
    """Remove the remaining equivalent states"""

    if DEBUG:
        print("\n\nRemove the remaining equivalent states:\n")

    for key, cell in reversed(table.items()):
        if key[0] != key[1] and cell.eq:
            if DEBUG:
                print(f"{states[key[1]]}: {cell.eq}")

            states.remove(states[key[1]])
