"""This program demonstrates one 
way to check for program arguments. It is missing
a function to check for the -f filename argument,
that students will implement."""

import sys  # required to pull args from command line

INPUT_PROMPT = "Enter text to analyze (STOP to end):"
END_WORD = "STOP"


def get_input() -> tuple:
    """
    Gets input from the client until the word STOP is entered on a
    single line in all caps. Each line is added to a list, then the
    tuple is returned. The STOP word is not included in the tuple.

    Examples: (note doctest is not run on this due to input prompt)
       Assume the client enters the following:
       Hello
       World
       STOP
       >> get_input()
       ('Hello', 'World')

       Assume the client enters the following:
       STOP
       >> get_input()
    """
    lines = []
    line = input(INPUT_PROMPT + "\n")
    while line != END_WORD:
        lines.append(line)
        line = input()
    return tuple(lines)


def read_file_to_tuple(file_name: str) -> tuple:
    """
    Reads a file into a tuple of strings, each string is a line from the file.

    Removes leading and trailing whitespace
    Skips blank lines

    Args:
        file_name (str): The name of the file to read.

    Returns:
        tuple: A list of strings, each string is a line from the file.
    """
    lines = []
    try :
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line:  # skip blank lines
                    lines.append(line.strip())  # remove leading and trailing whitespace
        return tuple(lines)
    except IOError as e:
        print(e)
        return tuple()


def check_args_for_count_option(argv: list) -> bool:
    """
    Checks to see if -c is in the args, if so, returns True.

    Args:
        argv (list): A list of command line arguments.

    Returns:
        bool: True if -c is in the args, False otherwise.
    """
    return "-c" in argv or "--count" in argv


def check_args_for_help(argv: list) -> bool:
    """
    Checks to see if -h is in the args, if so, prints the help message and returns True.

    Args:
        argv (list): A list of command line arguments.

    Returns:
        bool: True if -h is in the args, False otherwise.
    """
    if "-h" in argv or "--help" in argv:
        print_help()
        return True
    return False


def print_help() -> None:
    """
    Prints the help message for the program.
    """
    print("Usage: python args_tester.py [-h|--help] [-c|--count] [-f filename]")
    print("Options:")
    print(
        "  -f filename: The name of the file to print. Asks for client input if not provided."
    )
    print("  -h or --help: Print this help message and exit")
    print("  -c or --count: Count the lines in a poem")
    print("Also, a [] means the argument is optional.")


def check_args_for_filename(argv: list) -> str:
    """
    Checks to see if -f is in the args, if so, returns the filename.

    Args:
        argv (list): A list of command line arguments.

    Returns:
        str: The filename if -f is in the args, otherwise ''.
    """
    return ''
    ## replace with team code


def main(argv: list) -> None:
    if check_args_for_help(argv):
        return  # help is printed, exit program

    try:
        file = check_args_for_filename(argv)
    except ValueError as e:
        print(e) # print the error message
        print_help()
        return  # exit program
    
    if file:
        doc = read_file_to_tuple(file) 
    else:
        doc = get_input()

    if doc:
        print("\n".join(doc))

        if check_args_for_count_option(argv):
            print(f"Number of lines: {len(doc)}")

 


# It is common practice to grab the arguments in this
# part of the file, and just have main assume there is a
# list of strings with each argument. This makes it easier
# to reuse the main using different methods to get the args
# or just pass in a string list for testing.
if __name__ == "__main__":
    argv = sys.argv
    main(argv)
