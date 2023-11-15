arr = [[0, 0]]*10

for i in range(10):
    res = list(map(int, input().split()))
    arr[i] = [res[0], res[1]]
# init
res = [arr[0][1]]

# loop # 1 ~ 9
for i in range(1, 10):
    cnt = res[i-1] + arr[i][1] - arr[i][0]
    res.append(cnt)

print(max(res))
