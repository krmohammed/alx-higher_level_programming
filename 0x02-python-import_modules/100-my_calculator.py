#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calculator
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if sys.argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        print("{} + {} = {}".format(a, b, calculator.add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, calculator.sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, calculator.mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, calculator.div(a, b)))
