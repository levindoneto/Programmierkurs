#!/usr/local/bin/python3

'''
Build iteration tools.
'''

from typing import *
from progkurs import *
from itertools import islice

T = TypeVar("T")

def naturals(start: int=0):
    n = start
    while True:
        yield n
        n += 1


def iter_len(seq: Iterable[T]) -> int:
    '''
    The number of elements in a sequence. NB: This will exhaust generators!

    >>> g = (i**3 for i in range(100))
    >>> iter_len(g)  # test sanity
    100
    >>> iter_len(g)  # test exhaustion
    0
    '''
    #result = 0
    
    return sum(1 for _ in seq)

def take(n: int, seq: Iterable[T]) -> Iterable[T]:
    '''
    Yield at most(*) n elements from sequence seq.

    NB: DO NOT CREATE A LIST, only use iteration, counting and yield (i.e. *not* return).

    (*) If seq has fewer elements, only yield those.

    >>> type(take(10, range(10000))) is not list
    True

    >>> from string import ascii_letters
    >>> "|".join(take(10, ascii_letters))
    'a|b|c|d|e|f|g|h|i|j'

    >>> all(iter_len(take(n, seq))==n for seq in [range(1000), range(1000, 10000)] for n in range(100))
    True

    >>> list(take(0, range(10000))) == [] == list(take(0, range(10000)))
    True
    '''
    count = 0
    for el in seq:
        if (count<n):
            yield seq[count]
        else:
            continue
        count+=1


def drop(n: int, seq: Iterable[T]) -> Iterable[T]:
    '''
    Drop the first n elements from the sequence seq and yield the remaining elements (if any).

    NB: DO NOT CREATE A LIST, only use iteration, counting and yield (i.e. *not* return).

    >>> type(drop(10, range(10000))) is not list
    True

    >>> from string import ascii_letters

    >>> "|".join(drop(49, ascii_letters))
    'X|Y|Z'

    >>> "->".join(drop(2, "0123456789"))
    '2->3->4->5->6->7->8->9'

    >>> even = lambda x: x%2==0
    >>> list(take(10, filter(even, drop(50, naturals()))))
    [50, 52, 54, 56, 58, 60, 62, 64, 66, 68]
    '''
    #return islice(seq, n, None)

    count = 0
    for el in seq:
        if (count>=n):
            yield seq[count]
        count+=1
	
	
def test():
    import os, sys
    print("checking types")
    #assert os.system(sys.executable+' -m mypy '+__file__) == 0, "mypy could not verify types"

    import doctest
    doctest.testmod()
    print("OK")

if __name__ == '__main__':
	test()
