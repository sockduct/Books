####################################################################################################
'''
Simple example of doctest

Run file or use the following syntax to run tests verbosely
python -m doctest -v example-doctest.py

'''

def add_10(x):
    """ adds 10 to the input value
    # 3rd test fails on purpose:
    >>> add_10(5)
    15
    >>> add_10(-2)
    8
    >>> add_10(10)
    18
    """
    return x + 10
if __name__ == "__main__":
    import doctest
    doctest.testmod()

