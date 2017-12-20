#!/usr/local/bin/python3

"""
Silence exceptions within a context.
"""

from typing import *
from progkurs import *
import traceback


class SilenceException:
    def __init__(self, *exc_types):
        self.exc_types  = exc_types
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type: type, exc_val: Exception, exc_tb) -> bool:
        if exc_val == None:
            # no need to throw exception
            return True
        else:
            # go ahead and throw the exception raised
            return False


def consume(seq):
    """
    Consume all elements (and yield them) from sequence seq
    using only the next function, i.e. WITHOUT USING A FOR-LOOP OR COMPREHENSION.
    
    (Hint: You will need to catch an exception...)
    """
    seq = iter(seq)
    try:
        yield(seq)
        next()
    except:
        print("End of the sequence")		

def test_success():
    zeroname = SilenceException(ZeroDivisionError, NameError)
    ok = True
    with zeroname:
        print('a')
        try:
            print(1/0)
            print('b')
        except ZeroDivisionError as e:
            zeroname.__exit__(ZeroDivisionError, e, traceback.print_exc())

    with zeroname:
        try:
            print('1')
            print(1/x)
            print('2')
        except NameError as e:
            zeroname.__exit__(NameError, e, traceback.print_exc())

def test_failure():
    zeroname = SilenceException(ZeroDivisionError, NameError)
    try:
        with zeroname:
            print("before")
            with open("file-does-not-exist.txt") as f:
                data = f.read()
            print("after")
    except OSError:
        print("test_failure failed as expected")

def test():
    """
    >>> test_success()
    a
    1
    >>> test_failure()
    before
    test_failure failed as expected
    """
    import os, sys
    print("checking types")

    
    import doctest
    assert doctest.testmod() and print("doctests OK") is None
    
if __name__ == '__main__':
    test()