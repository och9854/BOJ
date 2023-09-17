import sys
n = int(input())
for _ in range(n):
    string = sys.stdin.readline().split()
    print(*(i[::-1] for i in string))
