import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    return_result = 0
    for ar_item in ar:
        return_result = return_result + ar_item
    return return_result

def main():
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    print(aVeryBigSum(ar))


if __name__ == '__main__':
    main()