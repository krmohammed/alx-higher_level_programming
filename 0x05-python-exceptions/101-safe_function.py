#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, TypeError, ValueError, ZeroDivisionError) as err_msg:
        sys.stderr.write("Exception: {}\n".format(err_msg))
