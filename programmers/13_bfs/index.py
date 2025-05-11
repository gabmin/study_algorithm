computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            BFS(n, computers, i, visited)
            answer += 1
    return answer

def BFS(n, computers, i, visited):
    visited[i] = True
    queue = deque([i])

    while queue:
        i = queue.popleft()
        visited[i] = True

        for j in range(n):
            if j != i and computers[i][j] == 1:
                if not visited[j]:
                    queue.append(j)

print('나의 정답 :', solution(n, computers), '/ 실제 정답: 2')