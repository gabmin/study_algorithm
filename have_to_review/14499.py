# 백준 주사위 굴리기
# https://www.acmicpc.net/problem/14499

from collections import deque
# import sys
# input = sys.stdin.readline
#
# n, m, x, y, k = map(int, input().split())
# game_map = [list(map(int, input().split())) for _ in range(n)]
# actions = list(map(int, input().split()))

n, m, x, y, k = 4, 2, 0, 0, 8
game_map = [
    [0, 2],
    [3, 4],
    [5, 6],
    [7, 8]
 ]
actions = [4, 4, 4, 1, 3, 3, 3, 2]

def solution(n, m, x, y, k, game_map, actions):
    dr = [None, 0, 0, -1, 1]
    dc = [None, 1, -1, 0, 0]
    r, c = x, y

    dice_vertical = deque([0, 0, 0, 0])
    dice_horizontal = deque([0, 0, 0, 0])

    for action in actions:
        new_r, new_c = r + dr[action], c + dc[action]

        if new_r < 0 or new_r >= n or new_c < 0 or new_c >= m:
            continue

        # 동
        if action == 1:
            target = dice_vertical.pop()
            dice_vertical.appendleft(target)
            dice_horizontal[1] = dice_vertical[1]
            dice_horizontal[3] = dice_vertical[3]
        # 서
        elif action == 2:
            target = dice_vertical.popleft()
            dice_vertical.append(target)
            dice_horizontal[1] = dice_vertical[1]
            dice_horizontal[3] = dice_vertical[3]
        # 남
        elif action == 3:
            target = dice_horizontal.pop()
            dice_horizontal.appendleft(target)
            dice_vertical[1] = dice_horizontal[1]
            dice_vertical[3] = dice_horizontal[3]
        # 북
        else:
            target = dice_horizontal.popleft()
            dice_horizontal.append(target)
            dice_vertical[1] = dice_horizontal[1]
            dice_vertical[3] = dice_horizontal[3]

        if game_map[new_r][new_c] == 0:
            game_map[new_r][new_c] = dice_vertical[3]
        else:
            dice_vertical[3] = game_map[new_r][new_c]
            dice_horizontal[3] = game_map[new_r][new_c]
            game_map[new_r][new_c] = 0

        r, c = new_r, new_c

        print(dice_vertical[1])


solution(n, m, x, y, k, game_map, actions)

n, m, x, y, k = 3, 3, 1, 1, 9
game_map = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8],
 ]
actions = [1, 3, 2, 2, 4, 4, 1, 1, 3]

print("-" * 10)
solution(n, m, x, y, k, game_map, actions)

n, m, x, y, k = 2, 2, 0, 0, 16
game_map = [
    [0, 2],
    [3, 4],
 ]
actions = [4, 4, 4, 4, 1, 1, 1, 1, 3, 3, 3, 3, 2, 2, 2, 2]

print("-" * 10)
solution(n, m, x, y, k, game_map, actions)
