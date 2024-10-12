# Task 1: Custom Module with Aliases 

    # Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.

def reverse(string):
    print(f"\nReversed String: \n{string[::-1]}")

def cap(string):
    print(f"\nCapitialized string: \n{string.capitalize()}")

def up_cased(string):
    print(f"\nUppercased string: \n{string.upper()}")