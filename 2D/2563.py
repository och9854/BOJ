wall = [[0 for _ in range(100)] for _ in range(100)]
N = int(input())
papers = []
for n in range(N):
    papers.append(list(map(int, input().split())))

for r, c in papers:  # 3, 7
    for i in range(10):
        for j in range(10):
            wall[r+i][c+j] = 1
print(sum(map(sum, wall)))
