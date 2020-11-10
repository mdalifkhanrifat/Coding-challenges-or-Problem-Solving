#!/bin/python3

import math
import os
import random
import re
import sys

def display(x):
    if x%2==0:
        if 2<=n<=5 or n>20:
            print("Not Weird")
        elif 6<=n<=20:
            print("Weird")  
    else:
        print("Weird")


if __name__ == '__main__':
    n = int(input().strip())
    display(n)
