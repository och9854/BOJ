from collections import deque


def bfs(x, y):
    size = 0
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2  # visited

    # loop
    while queue:  # queue가 있는 동안
        x, y = queue.popleft()
        size += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 < ny < m):  # in box range
                if (graph[nx][ny] == 1):  # not vistied
                    queue.append((nx, ny))
                    graph[nx][ny] = 2
    return size


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0  # 그림수
max_size = 0  # max

for i in range(n):
    for j in range(m):
        if (graph[i][j] == 1):  # IF not visited
            max_size = max(max_size, bfs(i, j))
            cnt += 1


print(cnt)
print(max_size)
