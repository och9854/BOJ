from collections import deque
import sys
n = int(input())
s = deque(input())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline()))


stack = deque()
while len(s) != 0:

    op = s.popleft()
    if 'A' <= op <= 'Z':  # 놓친부분 2. 세번비교? # num
        stack.append(nums[ord(op) - ord('A')])  # 놓친부분1: ord()
    else:  # operator
        num1, num2 = stack.pop(), stack.pop()
        if op == "*":
            res = num2*num1
        elif op == "/":
            res = num2/num1
        elif op == "+":
            res = num2 + num1
        else:
            res = num2 - num1

        stack.append(res)

print(f'{res:.2f}')
