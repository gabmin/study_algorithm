# 백준 구슬탈출2
# https://www.acmicpc.net/status?user_id=rlarkqals7&problem_id=13460&from_mine=1
from collections import deque

# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# game_map = [list(input().strip()) for _ in range(n)]

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def move_marble(r, c, move_r, move_c, game_map):
    move_count = 0

    while game_map[r + move_r][c + move_c] != "#" and game_map[r][c] != "O":
        r += move_r
        c += move_c
        move_count += 1

    return r, c, move_count

def is_available_to_take_out_only_red_marble(game_map):
    red_r, red_c = 0, 0
    blue_r, blue_c = 0, 0

    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "R":
                red_r, red_c = i, j

            if game_map[i][j] == "B":
                blue_r, blue_c = i, j

    queue = deque([[red_r, red_c, blue_r, blue_c, 1]])
    visited = []

    while queue:
        red_r, red_c, blue_r, blue_c, count = queue.popleft()

        if count > 10:
            break

        for index in range(4):
            new_red_r, new_red_c, red_count = move_marble(red_r, red_c, dr[index], dc[index], game_map)
            new_blue_r, new_blue_c, blue_count = move_marble(blue_r, blue_c, dr[index], dc[index], game_map)

            if game_map[new_blue_r][new_blue_c] == "O":
                continue

            if game_map[new_red_r][new_red_c] == "O":
                return count

            if new_red_r == new_blue_r and new_red_c == new_blue_c:
                if red_count > blue_count:
                    new_red_r -= dr[index]
                    new_red_c -= dc[index]
                else:
                    new_blue_r -= dr[index]
                    new_blue_c -= dc[index]

            new_position = [new_red_r, new_red_c, new_blue_r, new_blue_c, count + 1]
            visit_position = (new_red_r, new_red_c, new_blue_r, new_blue_c)

            if visit_position not in visited:
                visited.append(visit_position)
                queue.append(new_position)

    return -1

print(is_available_to_take_out_only_red_marble(game_map))  # 1 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = -1 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = 5 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))