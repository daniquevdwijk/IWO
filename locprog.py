# Author: Danique van der Wijk
# Date: 22-03-2021
# This program opens a textfile and checks if the geolocation has a value and is not equal to certain other values.

import sys


def main(argv):
    infile = open(argv[1], "r")
    for line in infile:
        l2 = line.split("\t")
        #print(l2)
        if len(l2) > 1:
            if l2[1] != '' and l2[1] != '\n':
                if l2[1] != 'Netherlands\n' and l2[1] != 'Nederland\n' and l2[1] != "The Netherlands" and l2[1] != "netherlands" and l2[1] != "Holland" and l2[1] != "holland":
                    print(line)

if __name__ == "__main__":
    main(sys.argv)
