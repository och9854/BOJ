a, b = map(int, input().split())
c = int(input())
n = int(input())

print(1 if b <= (c-a)*n and c >= a else 0)
