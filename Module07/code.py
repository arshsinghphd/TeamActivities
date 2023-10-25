"""
Module 07 sample code for CS 5001.
"""


def print_word(word: str) -> None:  
    """Prints a word shrinking by one letter each time on
    both sides of the world until there is nothing left.

    Args:
        word (str): the word to print

    """
    print(word)
    if len(word) <= 1:
        return None
    print_word(word[1:-1])


def reverse_string(string: str) -> str:
    """Recursively reverses a string.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("racecar")
        'racecar'

    Args:
        string (str): the string to reverse

    Returns:
        str: the reversed string
    """
    if len(string) <= 1:
        return string
    return string[-1] + reverse_string(string[:-1])


def factorial_iterative(n: int) -> int:
    """
    Gives the factorial for any number of
    n using an iterative solution.

    Examples:
        >>> factorial_iterative(1)
        1
        >>> factorial_iterative(4)
        24

    Args:
        n (int): the value to generate

    Returns:
        int: the factorial
    """
    counter = 2
    fact = 1
    while counter <= n:
        fact *= counter
        counter += 1
    return fact


def factorial(n: int) -> int:
    """
    Gives the factorial of any number using
    a recursive solution.

    Examples:
        >>> factorial(1)
        1
        >>> factorial(4)
        24

    Args:
        n (int): the value to generate

    Returns:
        int: the factorial
    """
    if n == 0 or n == 1:
        return 1  # done, exit the function immediately
    return n * factorial(n - 1)


def flatten(lst: tuple | list) -> list:
    """
    Flatten a tuple of tuples into a single list.

    Examples:
        >>> flatten((1, 2, (3, 4)))
        (1, 2, 3, 4)
        >>> flatten((1, (2, 3), (4, )))
        (1, 2, 3, 4)

    Args:
        lst (list): a tuple with one or more tuples inside of it

    Returns:
        tuple: a single tuple containing all the elements of the input tuples
    """
    if not lst:
        return []
    if isinstance(lst[0], tuple) or isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])  
    return list(lst[:1]) + flatten(lst[1:])  


# this example is a 'more advanced' concept, 
# here as it was talked about with students who asked
# but not expected to know or part of the team activity
def flatten_tail(lst: tuple | list) -> list:
    """
    Flatten a tuple of tuples into a single list.

    Examples:
        >>> flatten_tail((1, 2, (3, 4)))
        (1, 2, 3, 4)
        >>> flatten_tail((1, (2, 3), (4, )))
        (1, 2, 3, 4)

    Args:
        lst (list): a tuple with one or more tuples inside of it

    Returns:
        tuple: a single tuple containing all the elements of the input tuples
    """
    def flatten_tail_helper(lst: tuple | list, acc: list) -> list:
        if not lst:
            return acc
        if isinstance(lst[0], tuple) or isinstance(lst[0], list):
            return flatten_tail_helper(lst[0], flatten_tail_helper(lst[1:], acc))
        acc.append(lst[0])  # append the first element to the accumulator
        return flatten_tail_helper(lst[1:], acc)
    return flatten_tail_helper(lst, [])

def evaluate_expression(expression) -> int | float:
    """
    Evaluates a mathematical expression in the form of a tuple.

    Examples:
        >>> evaluate_expression(1)
        1
        >>> evaluate_expression((1, '+', 2))
        3
        >>> evaluate_expression((1, '+', (2, '*', 3)))
        7

    Args:
        expression: a tuple representing a mathematical expression

    Returns:
        int | float: the result of the expression
    """
    if isinstance(expression, int) or isinstance(expression, float):
        return expression  # base case
    elif isinstance(expression, tuple):
        left = evaluate_expression(expression[0])  # recursive call
        operator = expression[1]
        right = evaluate_expression(expression[2])  # recursive call
        return do_math(left, operator, right)
    return 0  # default case , not a good idea but works for now. Ideally this should raise an error!


def do_math(left: float | int, operator: str, right: float | int) -> float | int:
    """
    Performs a mathematical operation on two numbers.

    Examples:
        >>> do_math(1, '+', 2)
        3
        >>> do_math(1, '-', 2)
        -1
        >>> do_math(1, '*', 2)
        2
        >>> do_math(1, '/', 2)
        0.5

    Args:
        left: the left operand
        operator: the operator
        right: the right operand

    Returns:
        float | int: the result of the expression
    """
    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left * right
    elif operator == "/":
        return left / right  # yes this will error if right is 0
    return 0  # default case , not a good idea but works for now. Ideally this should raise an error!


# this main actually doesn't do anything other than run the doctest when the file is loaded
# this is another way to run them if you don't run it via the command line
# only makes sense if the file only has support functions and not a full program starting
# with main
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
