# 백준 촌수계산
# https://www.acmicpc.net/problem/2644

from collections import deque
import sys

# input = sys.stdin.readline
# n = int(input())
# t1, t2 = map(int, input().split())
# m = int(input())
# graph = [list(map(int, input().split())) for _ in range(m)]
#

n = 9
t1, t2 = 7, 3
m = 7
graph = [
    [1, 2],
    [1, 3],
    [2, 7],
    [2, 8],
    [2, 9],
    [4, 5],
    [4, 6],
]

def solution(n, t1, t2, graph):
    new_graph = [[] for _ in range(n + 1)]
    for x1, x2 in graph:
        new_graph[x1].append(x2)
        new_graph[x2].append(x1)

    queue = deque([[t1, 0]])
    visited = [t1]

    while queue:
        node, cnt = queue.popleft()

        if node == t2:
            return cnt

        for i in new_graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append([i, cnt + 1])



    return -1

print(solution(n, t1, t2, graph))

# n = 9
# t1, t2 = 8, 6
# m = 7
# graph = [
#     [1, 2],
#     [1, 3],
#     [2, 7],
#     [2, 8],
#     [2, 9],
#     [4, 5],
#     [4, 6]
# ]
#
# print(solution(n, t1, t2, graph))