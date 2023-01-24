#!/usr/bin/python3

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
    except Exception as error:
	import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
