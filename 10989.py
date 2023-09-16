# timeover
# import sys

# n = int(input())
# num = []
# for _ in range(n):
#     num.append(int(sys.stdin.readline()))


# print('\n'.join((str(i) for i in sorted(num))))

import sys
n = int(sys.stdin.readline())
nums = [0] * 10001
for i in range(n):
    nums[int(sys.stdin.readline())] += 1
for j in range(10001):
    if nums[j] != 0:
        for j in range(nums[j]):
            print(j)
