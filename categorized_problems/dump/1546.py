n = int(input())
scores = list(map(int, input().split()))
m = max(scores)  # max

print(sum(scores)*100/m/n)
