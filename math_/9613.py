import sys
import math
from itertools import combinations
t = int(sys.stdin.readline())

for i in range(t):
    case = list(map(int, sys.stdin.readline().split()))
    res = 0
    combs = combinations(case[1:], 2)
    for a, b in combs:
        res += math.gcd(a, b)
    print(res)
