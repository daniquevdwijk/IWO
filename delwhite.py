# Author: Danique van der Wijk
# Date: 22-03-2021
# This program opens a textfile and removes the whitelines.

import sys


def main(argv):
	infile = open(argv[1], "r")
	for line in infile:
		if line != "\n":
			print(line.strip())

		
if __name__ == "__main__":
    main(sys.argv)
