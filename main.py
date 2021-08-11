from debug import DEBUG
from file_utils import get_file_name, open_file, save_file
from implication_tables import (create_implication_table, create_states_table,
                                remove_eq_states, search_eq_states,
                                search_non_eq_next_states,
                                search_non_eq_states)

file_name = get_file_name()
input_matrix = open_file(file_name)
states = create_states_table(input_matrix)
table = create_implication_table(states)

if DEBUG:
    print("\n\nThe original states table:\n")
    for state in states:
        print(state)

search_non_eq_states(table)
search_non_eq_next_states(table)
search_eq_states(table)
remove_eq_states(table, states)

if DEBUG:
    print("\n\nThe new states table:\n")
    for state in states:
        print(state)

save_file("data/output.txt", states)
