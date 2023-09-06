"""
This file provides the code from the workshop.
"""
from typing import Dict, Any

EXAMPLES_MENU = \
""" 
Here are options for running examples, please select one or X to exit:
1. is_numeric_test - checks to see if an input isnumeric
2. test_number_print - Prints numbers divisible by the divisor
X. Exit the program
"""

def is_numeric_test() -> None:
    """Checks to see if an input isnumeric"""
    prompt = "Enter a value (x to stop): "
    value = input(prompt)
    while value != 'x':
        print(f"Is {value} numeric?", value.isnumeric())
        value = input(prompt)

def evens()-> None:
    """Prints even numbers from 0 to 10"""
    number_print()


def number_print(divisor: int = 2, max: int = 10, invert:bool= False) -> None:
    """Prints numbers divisible by the divisor, or prints numbers
    not divisible by the number if invert is True. 

    Args:
        divisor (int, optional): the number to look at. Defaults to 2.
        max (int, optional): the max numbers to print out to. Defaults to 10.
        invert (bool, optional): True if you want the numbers not divisible by divisor. Defaults to False.
    """
    counter = 0
    while(counter <= max):
        if (not invert) and counter % divisor == 0:
            print(counter)
        elif invert and counter % divisor != 0:
            print(counter)
        counter += 1

def test_number_print() -> None:
    """Function for testing the various options for number print using the menu system"""
    print("Default") 
    number_print()
    print()
    print("Print evens to 18")
    number_print(max=18)
    print()
    print("Div by 3")
    number_print(divisor=3)
    print()
    print("Odd numbers")
    number_print(invert=True)
    print()
    print("All numbers up to 9, not divisible by 3")
    number_print(3, 9, True)


def get_menu_item() -> str:
    """Gets a menu item for the examples menu"""
    print(EXAMPLES_MENU)
    while True:
        value = input("Enter a menu item: ").strip().casefold()
        if value == '1' or value == '2' or value == 'x':
            return value # exit the loop, and leave the function
        else:
            print("Invalid menu item, please try again.")
    


def main() ->  None:
    """Main driver, gives opportunity to load various examples"""
    print("Welcome to the examples program.")
    value = get_menu_item()
    while value != 'x':
        if value == '1':
            is_numeric_test()
        elif value == '2':
            test_number_print()
        value = get_menu_item()

    print("thank you.")


if __name__ == "__main__":
    main()