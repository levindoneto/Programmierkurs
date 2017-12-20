#!/usr/local/bin/python3

"""
A context for handling run time of code.
"""



from typing import *
from progkurs import *

T = TypeVar("T")
FilePath = str

import time

class timer:
    def __enter__(self):
        self.start = time.time()
        self.duration = None
        return self
    
    def __exit__(self, *exc_details):
        self.end = time.time()
        self.duration = self.end - self.start
    
    def __str__(self) -> str:
        now = time.time()
        if self.duration is not None and self.duration != 1:
            res = "Final duration: " + self.duration + "second " + 's' + "\nstart time: " + str(self.start) + "end time: " + str(self.end)
        elif self.duration is not None:
            res = "Final duration: " + self.duration + "second " + "\nstart time: " + str(self.start) + "\nend time: " + str(self.end)
        else:
            res = "Current duration: " + str(now) + "-" + str(self.start)
        return res


def check_timer():
    """
    >>> with timer() as t:
    ...     time.sleep(1)
    >>> assert 1 <= t.duration <= 1.2
    """
    pass


def count_comparisons(seq_gen: Iterable[T]) -> None:
    '''
    Compare counting methods using these approaches:
        1 "test_in"       ) "if k in d" test
        2 "get_default"   ) "d[k] = update(d.get(k, default))"
        3 "try"           ) "try: d[k] = update(1)" & catch exception
        4 "defaultdict"   ) specialized "defaultdict" data type
        5 "Counter" class ) specialized "Counter" class
        6 "count_method"  ) using "list.count(el)" method
    '''
    # 1
    seq = seq_gen()
    test_in_freq = {}
    with timer() as test_in_timer:
        for el in seq:
            if el in test_in_freq:
                test_in_freq[el] += 1
            else:
                test_in_freq[el] = 1
    # 2
    seq = seq_gen()
    get_default_freq = {}
    with timer() as get_default_timer:
        for el in seq:
            get_default_freq[el] = get_default_freq.get(el, 0) + 1
    # 3
    seq = seq_gen()
    try_freq = {}
    with timer() as try_timer:
        for el in seq:
            try:
                try_freq[el] += 1
            except KeyError:
                try_freq[el] = 1
    # 4
    from collections import defaultdict
    seq = seq_gen()
    defaultdict_freq = defaultdict(int)
    with timer() as defaultdict_timer:
        for el in seq:
            defaultdict_freq[el] += 1
    
    # 5
    from collections import Counter
    seq = seq_gen()
    with timer() as counter_timer:
        counter_freq = Counter(seq)
        counter_freq = str(counter_freq)
    
    # 6
    # seq = seq_gen()
    # with timer() as count_method_timer:
    #     seq_list = list(seq)
    #     count_method_freq = {el:seq_list.count(el) for el in seq_list}
    
    print("test_in_timer: ", test_in_timer)
    print("get_default_timer: ", get_default_timer)
    print("try_timer: ", try_timer)
    print("defaultdict_timer: ", defaultdict_timer)
    print("counter_timer: ", counter_timer)


def run_count_comparisons():
    ukwac_counts_fn = "ukwac-tok-lem.tok-len-4-6.subsel.sortNR.utf8"
    def tok_lem_pos_counts(fn: FilePath, encoding: str="utf8") -> Iterable[Tuple[str,str,str,int]]:
        with open(fn, encoding=encoding) as f:
            for line in f:
                c, t, l, p = line.split()
                c = int(c)
                yield (t, l, p, c)
    
    from operator import itemgetter
    toks   =  map(itemgetter(0), tok_lem_pos_counts(ukwac_counts_fn))
    lems   =  map(itemgetter(1), tok_lem_pos_counts(ukwac_counts_fn))
    pos    =  map(itemgetter(2), tok_lem_pos_counts(ukwac_counts_fn))
    counts =  map(itemgetter(3), tok_lem_pos_counts(ukwac_counts_fn))
    
    print("range: ", count_comparisons(lambda: range(int(10**5))))
    print("tokens: ", count_comparisons(toks))
    print("lemmas: ", count_comparisons(lems))
    print("parts-of-speech: ", count_comparisons(pos))
    print("counts: ", count_comparisons(counts))


def test():
    import os, sys
    print("checking types")

    import doctest
    assert doctest.testmod() and print("OK") is None


if __name__ == '__main__':
    test()
