# 백준 토마토
# https://www.acmicpc.net/problem/7569

from collections import deque
# import sys
# input = sys.stdin.readline
#
# m, n, h = map(int, input().split())
# box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

m, n, h = 5, 3, 1
box = [
   [[0, -1, 0, 0, 0],
    [-1, -1, 0, 1, 1],
    [0, 0, 0, 1, 1]]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution(m, n, h, box):


    queue = deque([])
    result = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    queue.append([i, j, k, 0])

    while queue:
        d, r, c, cnt = queue.popleft()

        for nd in [d + 1, d - 1]:
            if 0 <= nd < h:
                if box[nd][r][c] == 0:
                    box[nd][r][c] = 1
                    queue.append([nd, r, c, cnt + 1])
                    result = cnt + 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if box[d][nr][nc] == 0:
                    box[d][nr][nc] = 1
                    queue.append([d, nr, nc, cnt + 1])
                    result = cnt + 1

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return -1
    return result


print("정답: -1", "풀이:", solution(m, n, h, box))

m, n, h = 5, 3, 2
box = [
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
]

print("정답: 4", "풀이:", solution(m, n, h, box))

m, n, h = 4, 3, 2
box = [
    [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1],
        [-1, -1, -1, -1],
        [1, 1, 1, -1]
    ]
]

print("정답: 0", "풀이:", solution(m, n, h, box))