#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import *
    import sys

    command_argument = len(sys.argv) - 1

    if command_argument != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        
options = {"+": add, "-": sub, "*": mul, "/": div}

if sys.argv[2] not in list(options.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {}".format(a, sys.argv[2], b, end=" "))
    print(" = {}".format(options[sys.argv[2]](a, b)))
