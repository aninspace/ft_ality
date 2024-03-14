import sys
from parsing import parse_grammar_file
from training import start_training
from utility import print_machine_memory


def validate_and_process(grammar_file):
    if not grammar_file:
        return "Grammar file must be presented", None
    if not grammar_file.endswith(".gmr"):
        return "Wrong grammar file format", None

    machine_memory = parse_grammar_file(grammar_file)
    return None, machine_memory


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <grammar_file>")
        return

    error, machine_memory = validate_and_process(sys.argv[1])
    if error:
        print(error)
        return

    print("Starting analyzing grammar file...")
    print_machine_memory(machine_memory)
    print("Starting training...")
    start_training(machine_memory)


if __name__ == "__main__":
    main()
