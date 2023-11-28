import sys

n = int(input())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [0]*n
dp[0] = arr[0]

if n > 1:
    dp[1] = arr[0]+arr[1]
if n > 2:
    dp[2] = max(arr[2]+arr[1], arr[2]+arr[0], dp[1])  # skip (1st, 2nd, 3rd)

for i in range(3, n):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

print(dp[n-1])
