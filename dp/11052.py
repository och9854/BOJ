# init
n = int(input())
prices = [0]
prices += list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = prices[1]
dp[2] = max(prices[2], prices[1]*2)

for i in range(2, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + prices[j])


print(dp[n])
