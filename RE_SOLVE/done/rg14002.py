N = int(input())
A = list(map(int, input().split()))
LIS = [1]*N
# 1. save the length
for cnt in range(1, N):
    for prev in range(cnt):
        if A[cnt] > A[prev]:
            LIS[cnt] = max(LIS[cnt], LIS[prev]+1)

order = max(LIS)
print(order)

# 2. find the longest array
# solution 1
result = []
for idx in range(N-1, -1, -1):  # N-1 -> 0
    if LIS[idx] == order:  # 해당하는 순서를 찾았을 때
        result.append(A[idx])
        order -= 1

print(*result[::-1])
