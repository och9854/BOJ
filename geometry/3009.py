point_x = []
point_y = []
for i in range(3):
    x, y = map(int, input().split())
    point_x.append(x)
    point_y.append(y)


for x in point_x:
    if point_x.count(x) == 1:
        print(x, end=' ')


for y in point_y:
    if point_y.count(y) == 1:
        print(y)
