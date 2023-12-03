import sys

n = int(input())
book = []
for i in range(n):
    book.append([i]+sys.stdin.readline().split())
book = sorted(book, key=lambda x: (int(x[1]), int(x[0])))  # age, order

for _, i, j in book:
    print(i, j)
