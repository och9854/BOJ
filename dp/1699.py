n = int(input())
dp = [i for i in range(n+1)]

dp[1] = 1


for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1  # update dp[i]


print(dp[n])
'''
규칙을 살펴보자.
n   dp
1   1
2   2
3   3
4   1
5   2
6   3
7   4
8   2
9   1
10  2
11  3
12  4
13  2




'''
