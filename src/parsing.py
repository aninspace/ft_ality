import os
import re
import subprocess
from contextlib import contextmanager

actions_regex = re.compile(r"^(\w)->(\w+)$")
combinations_regex = re.compile(r"^([\w+]+)->(\w+)$")

def parse_grammar_file(grammar_file_path):
    with open_file(grammar_file_path) as content:
        # Split the content by newlines to get a list of lines
        print("hi")
        lines = content.splitlines()
        parsed_lines = list(map(parse_line, lines))
        actions, combinations = fold_lines(parsed_lines, ({}, {}), 0)
    return actions, combinations

def parse_line(line):
    actions_match = actions_regex.match(line)
    combinations_match = combinations_regex.match(line)
    if actions_match:
        return 'action', actions_match.groups()
    elif combinations_match:
        return 'combination', combinations_match.groups()
    else:
        return 'error', None

def fold_lines(parsed_lines, accumulators, index):
    if index >= len(parsed_lines):
        return accumulators

    line_type, content = parsed_lines[index]
    actions, combinations = accumulators

    if line_type == 'action':
        hook, action = content
        if hook in actions:
            actions[hook].append(action.replace("_", " "))
        else:
            actions[hook] = [action.replace("_", " ")]
    elif line_type == 'combination':
        hooks, action = content
        combinations[tuple(hooks.split("+"))] = action.replace("_", " ")

    return fold_lines(parsed_lines, (actions, combinations), index + 1)


@contextmanager
def open_file(file_name):
    try:
        # Use the appropriate command based on the operating system
        if os.name == 'posix':
            cmd = ['cat', file_name]
        elif os.name == 'nt':  # Windows
            cmd = ['type', file_name]
        else:
            raise OSError("Unsupported operating system")

        # Execute the command and capture the output
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Yield the output as a string
        yield result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error while reading file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
