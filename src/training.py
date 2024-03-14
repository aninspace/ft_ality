def start_training(machine_memory):
    def read_and_handle_input(states):
        user_input = input("Enter command: ")
        if user_input == 'q':
            print("Finishing training...")
            return

        new_states = states + [user_input]
        check_combinations(new_states, machine_memory[1], read_and_handle_input, machine_memory)

    read_and_handle_input([])


def check_combinations(states, combinations, callback, machine_memory):
    first_part_keys = machine_memory[0].keys()
    second_part_keys = machine_memory[1]

    possible_subsequences = (tuple(states[i:j]) for i in range(len(states)) for j in range(i + 1, len(states) + 1))

    valid_combinations = filter(
        lambda subseq: subseq in combinations and all(symbol in first_part_keys for symbol in subseq),
        possible_subsequences)

    first_valid_combination = next(valid_combinations, None)

    if first_valid_combination != None:
        print(second_part_keys[first_valid_combination])
        callback([])
    else:
        if states[-1] in machine_memory[0]:
            print(", ".join(machine_memory[0][states[-1]]))
        else:
            print("Unknown")
        callback(states)
