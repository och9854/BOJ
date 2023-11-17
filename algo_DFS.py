'''
DFS
- 스택 자료구조에 기초한다
- 실제로는 스택을 사용하지 않아도 되며, O(N)의 복잡도를 가진다.
- 실제 구현은 **재귀 함수**를 이용할 때 간단히 구현할 수 있다.
'''


def DFS1(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v)

    # 현재 노드와 "연결된 노드를 재귀 방문"
    for i in graph[v]:
        if not visited[i]:
            DFS1(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],      # 노드 1에 연결된 노드들
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

# 정의된 DFS 함수 호출
DFS1(graph, 1, visited)
