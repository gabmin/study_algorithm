# 백준 뱀
# https://www.acmicpc.net/problem/3190

from collections import deque
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# k = int(input())
#
# apples = [list(map(int, input().split())) for _ in range(k)]
#
# l = int(input())
#
# directions = [[int(x), y] for x, y in (input().split() for _ in range(l))]

n = 6
apples = [
    [3, 4],
    [2, 5],
    [5, 3]
]
directions = [
    [3, 'D'],
    [15, 'L'],
    [17, 'D']
]

def change_direction(d, x):
    if x == 'D':
        return (d + 1) % 4
    elif x == 'L':
        if d - 1 < 0:
            return 3
        return (d - 1) % 4
    return d


def solution(n, apples, directions):
    # 동남서북
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    game_map = [[0] * n for _ in range(n)]

    for r, c in apples:
        game_map[r - 1][c - 1] = 1

    queue = deque([[0, 0]])
    time = 0
    snake_direction = 0

    while True:
        r, c = queue[0]

        new_r, new_c = r + dr[snake_direction], c + dc[snake_direction]

        if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
            return time + 1

        if [new_r, new_c] in queue:
            return time + 1

        queue.appendleft([new_r, new_c])

        if game_map[new_r][new_c] == 1:
            game_map[new_r][new_c] = 0
        else:
            queue.pop()

        time += 1

        for t, d in directions:
            if time == t:
                snake_direction = change_direction(snake_direction, d)



print(solution(n, apples, directions))