import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = arr[:]

for i in range(n):
    for j in range(i):  # 자신이 가장 큰 숫자일때의 부분 수열을 구함
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))
