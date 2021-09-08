#!/usr/bin/python3
def print_last_digit(number):
    """ print the last digit and return it"""
    print("{}".format(number % 10), end="")
    return (abs(number % 10))
