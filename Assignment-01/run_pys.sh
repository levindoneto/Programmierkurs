#!/bin/bash

PYTHON3=/usr/local/bin/python3


ls *.py | egrep 'sol|ex' | while read f ; do
    echo '====' "$f"
    {
        $PYTHON3 -m mypy "$f" &&
        echo '----' passed typecheck &&
        $PYTHON3 "$f" &&
        echo '----' ran successfully
    }
done
    