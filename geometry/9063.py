point_x, point_y = [], []

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    point_x.append(x)
    point_y.append(y)

# min x, max x
print(f"{(max(point_x) - min(point_x))*(max(point_y) - min(point_y))}")
