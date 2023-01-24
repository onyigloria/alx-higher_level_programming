#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Executes a function safely.
    Args:
	fct: The function to execute.
	args: Arguments for fct.
    Returns:
	If an error occurs - None.
	otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
