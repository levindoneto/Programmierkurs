from typing import Iterable
#from progkurs import *

def even_sum(seq: Iterable[int]) -> int:
    """Returns the sum of all even numbers in the input sequence"""
    count = 0
    for i in seq:
        if (i%2 == 0):
            count+=i
    return count

def main():
    assert even_sum(range(9998)) == 24985002
    assert even_sum([20_000_000, -7, 2, 400, -16]) == 20000386

main()
