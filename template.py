#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Following PEP8 Style Guide and Google format function docstrings
    Docstring description of the script
"""

# Standard library imports one per line
import sys
import os

# Third party library imports one per line
import numpy

# Authorship constants
__authors__ = ['BA', 'JP']
__copyright__ = "Copyright 2020, NIU"
__credits__ = [None]
__version__ = "0.1"
__status__ = "Alpha"
__date__ = "28 February 2020"
__location__ = os.path.dirname(os.path.realpath(__file__))

# Global variables
my_int = 1
my_float = 1.01
my_string = "Hello World"
my_path = r"C:\Windows\System32"


def main(arg1):
    """
    Summary:
        `main` returns the (int) argument that it receives as a (float).

        Parameters:
            arg1 (int): Description of arg1.

        Returns:
            float: Description of return value.
    """

    return float(arg1)


if __name__ == '__main__':
    print(main.__doc__)  # Single line comment only for clarity, prints documentation for main function
    try:
        main(my_int)
    except Exception as e:
        sys.exit("Error running the main function: \n {}".format(e))
