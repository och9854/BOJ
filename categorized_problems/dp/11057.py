n = int(input())
dp = [1] * 10
for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j-1]
print(sum(dp) % 10007)

'''
timeover
n = int(input())
cnt = 0
if n == 1:
    print(10)
    exit()
for i in range(0, 10**n + 1):
    s = str(i)
    num = ''.join(sorted(s))
    if s == num:
        cnt += 1

        # print(s, num)

print(cnt)
'''
