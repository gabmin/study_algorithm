# 백준 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline

n = int(input())
hometown = [list(map(int, input().strip())) for _ in range(n)]

n = 7
hometown = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
]

def solution(n, hometown):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    visited = [[False] * n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if hometown[i][j] == 1 and visited[i][j] == False:
                stack = [[i, j]]
                count = 0
                visited[i][j] = True

                while stack:
                    r, c = stack.pop()
                    count += 1

                    for d in range(4):
                        new_r = r + dr[d]
                        new_c = c + dc[d]

                        if 0 <= new_r < n and 0 <= new_c < n and hometown[new_r][new_c] == 1:
                            if not visited[new_r][new_c]:
                                stack.append([new_r, new_c])
                                visited[new_r][new_c] = True

                result.append(count)

    result.sort()
    print(len(result))
    for r in result:
        print(r)

solution(n, hometown)





