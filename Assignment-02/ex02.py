from typing import Iterable, List
#from progkurs import *

def normalize(seq1: Iterable[int]) -> List[float]:
    """Normalizes the values in seq1 to values in the range [0,1],
    so that the normalized values add up to 1.
    """
    # Don't worry about negative numbers in the input!
    sumOfSeqOne = sum(seq1)
    result = []
    for number in seq1:
        result.append(number/sumOfSeqOne)
    #print ("result: ", result)
    return result


def main():
    assert normalize([1, 1]) == [0.5, 0.5]
    assert normalize([7, 7]) == [0.5, 0.5]
    assert normalize([3, 9]) == [0.25, 0.75]
    assert normalize([12, 3]) == [0.8, 0.2]
    assert normalize(range(5)) == [0.0, 0.1, 0.2, 0.3, 0.4]

main()
