# 백준 빙상
# https://www.acmicpc.net/problem/2573

from collections import deque
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# ice_map = [list(map(int, input().split())) for _ in range(n)]

n, m = 5, 7
ice_map = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 2, 4, 5, 3, 0, 0],
    [0, 3, 0, 2, 5, 2, 0],
    [0, 7, 6, 2, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(n, m, current_ice_map):
    queue = deque([])
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = 0

    for r in range(n):
        for c in range(m):
            if current_ice_map[r][c] != 0 and not visited[r][c]:
                visited[r][c] = True
                queue.append((r, c))
                result += 1

                while queue:
                    row, cul = queue.popleft()

                    for i in range(4):
                        new_r = row + dr[i]
                        new_c = cul + dc[i]

                        if 0 <= new_r < n and 0 <= new_c < m:
                            if current_ice_map[new_r][new_c] != 0 and not visited[new_r][new_c]:
                                queue.append([new_r, new_c])
                                visited[new_r][new_c] = True

    return result

def melt_ice(n, m, melted_ice_map):

    new_map = [[0 for _ in range(m)] for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if melted_ice_map[r][c] != 0:
                count = 0

                for i in range(4):
                    new_r = r + dr[i]
                    new_c = c + dc[i]

                    if 0 <= new_r < n and 0 <= new_c < m:
                        if melted_ice_map[new_r][new_c] == 0:
                            count += 1

                current = melted_ice_map[r][c]
                diff = current - count

                if diff > 0:
                    new_map[r][c] = diff
    return new_map


def solution(n, m, ice_map):
    ice = ice_map
    time = 0
    while True:
        ice_block = bfs(n, m, ice)

        if ice_block == 0:
            return 0

        if ice_block >= 2:
            return time



        ice = melt_ice(n, m, ice)
        time += 1


print("정답: 2", "풀이:", solution(n, m, ice_map))
