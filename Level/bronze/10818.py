import math
n = int(input())
arr = list(map(int, input().split()))
res = [-math.inf, math.inf]  # max, min

for i in arr:
    # check min: res[0] > i -> update
    if i < res[1]:
        res[1] = i

    if i > res[0]:
        res[0] = i

print(res[1], res[0])
