N = int(input())
price = [0] + list(map(int, input().split()))
dp = [10001] * (N+1)
dp[0] = 0
dp[1] = price[1]
dp[2] = min(price[2], price[1] * 2)

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + price[j])

print(dp[-1])
