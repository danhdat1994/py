#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input().strip())
a=range(6,20)
if n%2!=0:
    print('Weird')
elif n in range(2,5):
    print('Not Weird')
elif n in range(6,21):
    print('Weird')
else:
    print('Not Weird')