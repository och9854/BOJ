# s3
case = int(input())
dp = [1] * 12
dp[0] = 0
dp[2] = 2
dp[3] = 4

for c in range(case):
    n = int(input())
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])
