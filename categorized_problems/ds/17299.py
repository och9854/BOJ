import sys
from collections import Counter
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
answer = [-1]*n
counts = Counter(nums)
# print(counts)


stack = []
stack.append(0)
for i in range(1, n):
    while stack and counts[nums[stack[-1]]] < counts[nums[i]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
