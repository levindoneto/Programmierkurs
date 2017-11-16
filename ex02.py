#!/usr/local/bin/python3

from typing import *
from progkurs import *

def count(nums):
    res = 0
    for num in nums:
        res = res + 1
    return res

def total(nums):
    res = 0
    for num in nums:
        res = res + num
    return res

def average(nums):
    return total(nums) / count(nums)

def test01():
    return 10 == count(range(10))

def test02():
    return 2.5 == average([1,2,3,4])

def test03():
    return 10 == total([1.0, 2.0, 3, 4])


def run_tests(show_passed=False, show_failed=True):
    tests = [test01, test02, test03]
    all_passed = True

    for test in tests:
        test_run = test()
        if not test_run:
            all_passed = False
            if show_failed:
                print("Ein Fehler wurde gefunden")
        elif test_run and show_passed:
            print("Alles ok")
    return all_passed


def main():
    if not __debug__:
        # alert on all single tests
        response = run_tests()
    elif __debug__:
        # alert failed single tests
        response = run_tests(False, False)
    else:
        # silent on single tests
        response = run_tests(fill(____))
    if response: print("passed all tests")

if __name__ == '__main__':
    main()
