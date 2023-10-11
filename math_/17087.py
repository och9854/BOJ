from math import gcd

N, S = list(map(int, input().split()))
kids = list(map(int, input().split()))
ans = abs(S-kids[0])

if S == 1:
    print(ans)
else:
    for i in range(1, N):
        ans = gcd(ans, abs(S-kids[i]))

    print(ans)
