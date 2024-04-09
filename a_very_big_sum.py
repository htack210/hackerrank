#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    big_sum = 0
    for i in range(0, len(ar)):
        big_sum += ar[i]
    return big_sum


def main():
    print(aVeryBigSum([1000000001, 1000000002,
          1000000003, 1000000004, 1000000005]))


main()
