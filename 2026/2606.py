# 백준 바이러스
# https://www.acmicpc.net/problem/2606

from collections import deque
# import sys
# input = sys.stdin.readline
#
# c = int(input())
# l = int(input())
# network = [list(map(int, input().split())) for _ in range(l)]

c = 7
l = 6
network = [
    [1, 2],
    [2, 3],
    [1, 5],
    [5, 2],
    [5, 6],
    [4, 7]
]

graph = [[] for _ in range(c + 1)]

for i in range(l):
    graph[network[i][0]].append(network[i][1])
    graph[network[i][1]].append(network[i][0])

queue = deque([1])
visited = [1]

while queue:
    node = queue.popleft()

    for target in graph[node]:
        if target not in visited:
            queue.append(target)
            visited.append(target)


print(len(visited) - 1)


