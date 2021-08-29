from debug import DEBUG
from file_utils import get_file_name, get_input_from_file, save_states_to_file
from implication_tables import (create_states_table,
                                implication_table_from_states,
                                remove_remaining_eq_states,
                                search_eq_states_on_vacant_cells,
                                search_non_eq_states,
                                search_non_eq_states_on_vacant_cells)

file_name = get_file_name()
input_matrix = get_input_from_file(file_name)
states = create_states_table(input_matrix)
table = implication_table_from_states(states)

if DEBUG:
    print("\n\nThe original states table:\n")
    for state in states:
        print(state)

search_non_eq_states(table)
search_non_eq_states_on_vacant_cells(table)
search_eq_states_on_vacant_cells(table)
remove_remaining_eq_states(table, states)

if DEBUG:
    print("\n\nThe new states table:\n")
    for state in states:
        print(state)

save_states_to_file("data/output.txt", states)
