# 백준 미로 탐색
# https://www.acmicpc.net/problem/2178

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

miro = [list(map(int, input().strip())) for _ in range(n)]

n, m = 4, 6
miro = [
    [1,0,1,1,1,1],
    [1,0,1,0,1,0],
    [1,0,1,0,1,1],
    [1,1,1,0,1,1]
]

def solution(n, m, map):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    queue = deque([[0, 0, 1]])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        r, c, cnt = queue.popleft()

        if r == n - 1 and c == m - 1:
            return cnt

        for i in range(4):
            new_r, new_c = r + dr[i], c + dc[i]

            if 0 <= new_r < n and 0 <= new_c < m and map[new_r][new_c] == 1:
                if not visited[new_r][new_c]:
                    visited[new_r][new_c] = True
                    queue.append([new_r, new_c, cnt + 1])


print(solution(n, m, miro))

