#!/usr/local/bin/python3

from typing import *

def count(nums: int) -> int:
    res = 0
    for num in nums:
        res = res + 1
    return res

def total(nums: Iterator[int]) -> int:
    res = 0
    for num in nums:
        res = res + num
    return res

def average(nums: int) -> float:
    return total(nums) / count(nums)

def main():
    print(average(list(range(100))))     # erster Aufruf
    print(average(tuple(range(100))))    # zweiter Anruf
    print(average(range(100)))           # dritter Anruf
    return

if __name__ == '__main__':
    main()
