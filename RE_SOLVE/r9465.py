import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    # get N
    n = int(input())
    # get arr
    dp = [list(map(int, input().split())) for _ in range(2)]

    # calculate
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        # init
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        # iter
        for i in range(2, n):
            dp[0][i] += max(dp[1][i-2], dp[1][i-1])
            dp[1][i] += max(dp[0][i-2], dp[0][i-1])

    # print result
    print(max(dp[0][n-1], dp[1][n-1]))
