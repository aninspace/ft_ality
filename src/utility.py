def print_machine_memory(machine_memory):
    actions, combinations = machine_memory

    # Actions
    print("Actions:")
    actions_output = "\n".join(f"{hook} --> {', '.join(actions_list)}" for hook, actions_list in actions.items())
    print(actions_output)

    # Combinations
    print("Combinations:")
    combinations_output = "\n".join(f"{' + '.join(hooks)} --> {action}" for hooks, action in combinations.items())
    print(combinations_output)


