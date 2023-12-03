# failed: timeover O(N^2)
# from collections import deque
# import sys
# n = int(input())
# nums = deque(map(int, sys.stdin.readline().split()))
# nge = [-1]*n  # n+1개, 마지막 건 출력x

# for i in range(n-1):
#     tmp = nums.popleft()  # each number

#     # use memory
#     if tmp < nge[i-1] and i != 0:
#         nge[i] = nge[i-1]
#         break
#     # traverse
#     else:
#         for j in nums:
#             if j > tmp:
#                 nge[i] = j
#                 break

# for s in nge:
#     print(s, end=' ')


# answer
# gold 4
import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nge = [-1]*n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and nums[stack[-1]] < nums[i]:
        nge[stack.pop()] = nums[i]
    stack.append(i)

print(*nge)
