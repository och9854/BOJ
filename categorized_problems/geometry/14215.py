# ans1
a, b, c = map(int, input().split())
tri = sorted([a, b, c], reverse=True)
sum = sum(tri)
while True:
    if 2*tri[0] < sum:
        print(sum)
        break
    else:
        tri[0] -= 1
        sum -= 1


# ans2
a, b, c = sorted(map(int, input().split()))
print(a + b + min(c, a+b-1))
