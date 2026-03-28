# 백준 DFS와 BFS
# https://www.acmicpc.net/problem/1260

from collections import deque
# import sys
# input = sys.stdin.readline
#
# n, m, v = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(m)]

n, m, v = 4, 5, 1
graph = [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 4],
    [3, 4]
]

new_graph = [[] for _ in range(n + 1)]
for i in range(len(graph)):
    new_graph[graph[i][0]].append(graph[i][1])
    new_graph[graph[i][1]].append(graph[i][0])

for j in range(n + 1):
    new_graph[j].sort()

def dfs():
    stack = [v]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            for target in reversed(new_graph[node]):
                if target not in visited:
                    stack.append(target)

    return " ".join(map(str, visited))


def bfs():
    queue = deque([v])
    visited = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for target in new_graph[node]:
                if target not in visited:
                    queue.append(target)

    return " ".join(map(str, visited))


print(dfs())
print(bfs())




