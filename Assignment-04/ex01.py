#!/usr/local/bin/python3

"""
In NLP, evaluation metrics play an important role.
They help researcher guage the adequacy of models
such as classifiers and allow the comparison of
different approaches to solving a task.

Among the most commonly used metrics are:

- accuracy (percentage of accurate predictions made)
- precision (percentage of accurate positive predictions)
- recall (percentage of actual positive predictions correctly made)
- f-score (balances precision and recall).

Please refer to the docstrings. Tests will be run
(on all exercises ex01.py, ex01.py and ex03.py) by
simply running the program.
"""


from typing import *
#from progkurs import *
T = TypeVar("T")
Count = int

def accuracy(classifications, gold): # Ok
    """
    >>> accuracy([], []) # zero predictions are taken to be accurate ones.
    1.0
    >>> accuracy("AABB", "ABAB")
    0.5
    >>> accuracy("AAAAAA", "BBBBBB")
    0.0
    >>> accuracy("AACAA", "BBCBB")
    0.2
    >>> even = lambda x: x%2==0
    >>> odd  = lambda x: not even(x)
    >>> nums = range(100)
    >>> accuracy(filter(even, nums), filter(odd, nums))
    0.0
    """
    correct = 0
    incorrect = 0
    result = 1.0

    for c, g in zip(classifications, gold):
        if c == g:
            correct += 1
        else:
            incorrect += 1
    if correct + incorrect > 0:
        result = correct / (correct + incorrect)
    return result

def pr_stats(judgments, gold): # Ok
    """
    Counts upon which, precision and recall values can be calculated.
    (cf. https://en.wikipedia.org/wiki/Precision_and_recall )
    """
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0

    for j, g in zip(judgments, gold):
        if j: # positive
            if g:
                true_positives += 1 # relevant
            else:
                false_positives += 1 # not relevant
        else:
            if g: # negative
                false_negatives += 1 # relevant
            else:
                true_negatives += 1 # not relevant

    return dict(tp=true_positives,
                fp=false_positives,
                tn=true_negatives,
                fn=false_negatives)

def precision_from_stats(stats): # Ok

    #Calculate precision based on output from pr_stats.
    """
    match = dict(judgments=[True, False], gold=[True, False])
    match_stats = pr_stats(**match)
    precision_from_stats(match_stats)
    #1.0
    >>> no_match = dict(judgments=[True, False], gold=[False, True])
    >>> no_match_stats = pr_stats(**no_match)
    >>> precision_from_stats(no_match_stats)
    0.0
    >>> half_match1 = dict(judgments=[True, False], gold=[True, True])
    >>> half_match1_stats = pr_stats(**half_match1)
    >>> precision_from_stats(half_match1_stats)
    1.0
    >>> half_match2 = dict(judgments=[True, False], gold=[False, False])
    >>> half_match2_stats = pr_stats(**half_match2)
    >>> precision_from_stats(half_match2_stats)
    0.0
    >>> half_match3 = dict(judgments=[True, False, True, False], gold=[True, True, False, False])
    >>> half_match3_stats = pr_stats(**half_match3)
    >>> precision_from_stats(half_match3_stats)
    0.5
    >>> half_match4 = dict(judgments=[True, False, True, False], gold=[False, False, True, True])
    >>> half_match4_stats = pr_stats(**half_match4)
    >>> precision_from_stats(half_match4_stats)
    0.5
    """
    result = 1.0
    tp, fp, tn, fn = map(stats.get, "tp fp tn fn".split())
    if((tp + fp) > 0):
        result = tp / (tp + fp) # precision or positive predictive value
    return result

def recall_from_stats(stats): # Ok
    """
    Calculate recall based on output from pr_stats.

    >>> match = dict(judgments=[True, False], gold=[True, False])
    >>> match_stats = pr_stats(**match)
    >>> recall_from_stats(match_stats)
    1.0
    >>> no_match = dict(judgments=[True, False], gold=[False, True])
    >>> no_match_stats = pr_stats(**no_match)
    >>> recall_from_stats(no_match_stats)
    0.0
    >>> half_match1 = dict(judgments=[True, False], gold=[True, True])
    >>> half_match1_stats = pr_stats(**half_match1)
    >>> recall_from_stats(half_match1_stats)
    0.5
    >>> half_match2 = dict(judgments=[True, False], gold=[False, False])
    >>> half_match2_stats = pr_stats(**half_match2)
    >>> recall_from_stats(half_match2_stats)
    1.0
    >>> half_match3 = dict(judgments=[True, False, True, False], gold=[True, True, False, False])
    >>> half_match3_stats = pr_stats(**half_match3)
    >>> recall_from_stats(half_match3_stats)
    0.5
    >>> half_match4 = dict(judgments=[True, False, True, False], gold=[False, False, True, True])
    >>> half_match4_stats = pr_stats(**half_match4)
    >>> recall_from_stats(half_match4_stats)
    0.5
    """
    result = 1.0
    tp, fp, tn, fn = map(stats.get, "tp fp tn fn".split())
    if tp + fn > 0:
        result = tp / (tp + fn)
    return result

def fscore_from_stats(stats, beta): # Ok
    """
    Calculate fscore -- with parameter beta! -- from pr_stats output.
    (cf. https://en.wikipedia.org/wiki/F1_score )
    """
    result = 1.0
    p, r = (f(stats) for f in (precision_from_stats, recall_from_stats))
    if p * r > 0:
        result = ((1 + beta*beta)*((p*r)/((beta*beta)*p)+r))
    return result

def test():
    import doctest
    doctest.testmod(verbose=False)

if __name__ == '__main__':
    test()
