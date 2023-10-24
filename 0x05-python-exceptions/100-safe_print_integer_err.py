#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err_msg:
        sys.stderr.write("Exception: {}\n".format(err_msg))
        return False
    else:
        return True
