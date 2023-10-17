n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
