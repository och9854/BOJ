import sys
n = int(input())
arr = [0] * (1000001)
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 1000001):
    arr[i] = (arr[i-1] + arr[i-2] + arr[i-3]) % 1000000009


for i in range(n):
    num = int(sys.stdin.readline())
    print(arr[num])
