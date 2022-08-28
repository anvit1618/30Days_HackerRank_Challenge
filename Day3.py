#!/bin/python3

import math
import os
import random
import re
import sys

def solve(N):
    
    while (N % 2) == 0:
        if (2<N<=5):
            print("Not Weird")
            break
        elif (6<N<=20):
            print("Weird")
            break
        elif (N>20):
            print("Not Weird")
            break
    
    if (N % 2) != 0:
        print("Weird")

    return 0
if __name__ == '__main__':
    N = int(input().strip())
    solve(N)
