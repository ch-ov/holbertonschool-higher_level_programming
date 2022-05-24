#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = None
    try:
        result = fct(*args)
    except Exception as error:
        print("Exception: {}".format(str(error)), file=sys.stderr)
    return (result)
