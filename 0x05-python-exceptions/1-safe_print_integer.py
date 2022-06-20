#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format()
    Args:
        value: integer to be printed

    Returns:
        True if the value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        is_integer = True
    except ValueError:
        is_integer = False

    return (is_integer)
