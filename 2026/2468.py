# 백준 2468 안전 영역
# https://www.acmicpc.net/problem/2468

from collections import deque
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# city_map = [list(map(int, input().split())) for _ in range(n)]

n = 5
city_map = [
    [6, 8, 2, 6, 2],
    [3, 2, 3, 4, 6],
    [6, 7, 3, 3, 2],
    [7, 2, 5, 3, 6],
    [8, 9, 5, 2, 7]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, visited, city_map, height):
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and city_map[nr][nc] >= height:
                queue.append((nr, nc))
                visited[nr][nc] = True

def solution(n, city_map):
    result = 1
    height = 1

    while height <= 100:
        visited = [[False for _ in range(n)] for _ in range(n)]
        region = 0

        for i in range(n):
            for j in range(n):
                if city_map[i][j] >= height and not visited[i][j]:
                    dfs(i, j, visited, city_map, height)
                    region += 1

        result = max(result, region)

        height += 1

    return result


print("정답: 5", "풀이:", solution(n, city_map))

n = 7
city_map = [
    [9, 9, 9, 9, 9, 9, 9],
    [9, 2, 1, 2, 1, 2, 9],
    [9, 1, 8, 7, 8, 1, 9],
    [9, 2, 7, 9, 7, 2, 9],
    [9, 1, 8, 7, 8, 1, 9],
    [9, 2, 1, 2, 1, 2, 9],
    [9, 9, 9, 9, 9, 9, 9]
]

print("정답: 6", "풀이:", solution(n, city_map))