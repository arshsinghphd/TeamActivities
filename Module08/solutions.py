"""Solution file for student work
"""
import sys

def average(values: tuple) -> float:
    if len(values) == 0:
        raise ValueError("Cannot average an empty tuple")
    return sum(values) / len(values)


def check_args_for_filename(argv: list) -> str:
    """
    Checks to see if -f is in the args, if so, returns the filename.

    Args:
        argv (list): A list of command line arguments.

    Returns:
        str: The filename if -f is in the args, otherwise ''.
    """
    if "-f" in argv:
        index = argv.index("-f")
        if len(argv) > index + 1 and not argv[index + 1].startswith("-"):
            return argv[index + 1]
        else:
            raise ValueError("Missing filename after -f")
    return ""


def main(argv):
    for arg in argv:
        print(arg)


if __name__ == "__main__":
    main(sys.argv)
