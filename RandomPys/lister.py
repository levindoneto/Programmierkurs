#!/usr/local/bin/python3

"""
lister

Usage:
    lister ls   <dir>       [--recursive]
    lister find <pat> <dir> [--type=(f|d)] [--recursive]

Options:
    --type=<type>  [Default: f]
"""

from typing import *
import sys
import os
import re

def ls(dir:str, recursive:bool) -> Iterable[str]:
    if recursive:
        for path, dirs, fns in os.walk(dir):
            for item in dirs+fns:
                yield os.path.join(path, item)
    else:
        for item in os.listdir(dir):
            yield os.path.join(dir, item)

def find(pat:str, dir:str, typ:str, recursive:bool) -> Iterable[str]:
    assert typ in ('f', 'd')
    typecheck = os.path.isfile if typ=='f' else os.path.isdir
    if not recursive:
        for item in ls(dir=dir, recursive=False):
            if re.fullmatch(pat, item) and typecheck(item):
                yield os.path.join(dir, item)
    else:
        for (path, dirs, fns) in os.walk(dir):
            if typ is 'd':
                found = dirs
            elif typ is 'f':
                found = fns
            for fn in found:
                if re.fullmatch(pat, fn):
                    yield os.path.join(path, fn)



def main(opts) -> None:
    if opts['ls']:
        results = ls(opts['<dir>'], opts['--recursive'])
    elif opts['find']:
        results = find(opts['<pat>'], opts['<dir>'], typ=opts['--type'], recursive=opts['--recursive'])
    else:
        raise NotImplementedError("This should only be reached if we add commands to __doc__!")
    for result in results:
        print(result)

if __name__ == '__main__':
    import docopt
    opts = docopt.docopt(__doc__)
    # print(opts)
    main(opts)
