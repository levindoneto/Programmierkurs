import sys

''' To use:
	python piping.py < inputFile > outputFile '''

for l in sys.stdin:
	sys.stdout.write(l.lower())