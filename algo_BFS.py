##########################################################################################
# PRACTICE PART
from collections import deque
# case1. 1D BFS


def BFS1(graph, start, visited):
    # init
    queue = deque()
    queue.append(start)
    visited[start] = 1  # visited

    # while loop
    while queue:  # 큐가 빌 때까찌
        v = queue.popleft()  # 큐에서 하나 뻄
        print(v)

        # update for next BFS
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
BFS1(graph, 1, visited)


# case2. 2D BFS: 사각형 순환

def BFS2(x, y):
    # init
    queue = deque()
    queue.append(x, y)
    graph[x][y] = True  # visited: depends on the value in graph

    # loop
    while queue:
        x, y = queue.popleft()
        print(x, y)

        # update for next curr
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n and 0 <= ny < m):  # IF in box range
                if graph[nx][ny] == False:  # IF not visited
                    queue.append((nx, ny))
                    graph[nx][ny] = True


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
