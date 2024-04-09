#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


def rotateLeft(d, arr):
    tmp = 0
    for _ in range(d):
        tmp = arr.pop(0)
        arr.append(tmp)
    return arr


def main():
    print(rotateLeft(2, [1, 2, 3, 4, 5]))


main()
