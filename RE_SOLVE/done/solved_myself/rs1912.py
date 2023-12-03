n = int(input())
arr = list(map(int, input().split()))
dp = arr

for i in range(1, n):
    # update max( 이전 arr값 + dp 값, dp값)
    dp[i] = max(arr[i-1] + dp[i], dp[i])

print(max(dp))
