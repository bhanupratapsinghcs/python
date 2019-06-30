import math
import os
import random
import re
import sys


def solve(s):
    full_name = s.split(' ')
    print(full_name)
    return ' '.join((word.capitalize() for word in full_name))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "Hello   World  Lol 3g"
    print(solve(s))
    # print(s)

    # result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
