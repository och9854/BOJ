import sys

dp = [[0, 0, 0] for _ in range(100001)]
# init
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

# loop
for i in range(4, 100001):
    # n-1 에서 +1: 1로 끝나지 않은 값들
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009  # n-2 에서 +2
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009  # n-3 에서 +3

n = int(input())

for i in range(n):
    num = int(sys.stdin.readline())
    print(sum(dp[num]) % 1000000009)
