#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def reverseArray(a):
    reverse = []
    i = 0
    j = -1
    while i < len(a):
        reverse.append(a[j])
        j += -1
        i += 1
    return reverse


def main():
    print(reverseArray([1, 2, 3, 4]))


main()
