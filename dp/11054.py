import sys
n = int(input())
arr_front = list(map(int, input().split()))
arr_rear = arr_front[::-1]
dp_front = [1 for i in range(n)]  # init with len 1
dp_rear = [1 for i in range(n)]  # init with len 1

for i in range(n):
    for j in range(i):
        if arr_front[j] < arr_front[i]:
            dp_front[i] = max(dp_front[i], dp_front[j]+1)
        if arr_rear[j] < arr_rear[i]:
            dp_rear[i] = max(dp_rear[i], dp_rear[j]+1)


result = []
for i in range(n):
    result.append(dp_front[i] + dp_rear[::-1][i]-1)

print(max(result))
