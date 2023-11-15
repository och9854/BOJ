n = int(input())
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))


for i, j in sorted(points, key=lambda x: (x[0], x[1])):
    print(i, j)
