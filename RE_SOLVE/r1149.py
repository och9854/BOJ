import sys
n = int(input())
arr = []
res = 0

for i in range(n):  # n loops
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

print(min(arr[n-1]))

# mistake: thought RGB in 3 set..!
