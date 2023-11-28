# import sys
# n = int(input())
# arr = list(map(int, input().split()))
# if n == 1:
#     print(arr[0])
#     exit()

# dp = [[0] for i in range(n)]  # init with len 1

# for i in range(n):
#     tmp = []
#     for j in range(i):
#         if arr[j] > arr[i]:  # 30 > 10 , 20 > 10
#             tmp.append(arr[j])  # [].append(30)
#             # 길이가 더 긴 리스트 반환
#             longer = sorted([list(set(tmp)), list(set(dp[j]))],
#                             key=len, reverse=True)[0]
#             # dp update
#             dp[i] = longer
#     dp[i].append(arr[i])

# print(len(max(dp, key=len)))

#
import sys
n = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(n)]  # init with len 1

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
