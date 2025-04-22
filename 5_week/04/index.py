k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동: 1 서: 2 북: 3 남: 4
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def back_direction(d):
    if d % 2 == 0:
        return  d + 1
    else:
        return d - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1

    stack = [[[] for _ in range(n)] for _ in range(n)]

    for index in range(horse_count):
        r, c, d = horse_location_and_directions[index]
        stack[r][c].append(index)

    while turn_count <= 1000:
        for index in range(horse_count):
            r, c, d = horse_location_and_directions[index]

            new_r = r + dr[d]
            new_c = c + dc[d]

            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = back_direction(d)
                horse_location_and_directions[index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            moving_horse_array = []

            for i in range(len(stack[r][c])):
                current_index = stack[r][c][i]

                if index == current_index:
                    moving_horse_array = stack[r][c][i:]
                    stack[r][c] = stack[r][c][:i]
                    break

            if game_map[new_r][new_c] == 1:
                moving_horse_array = reversed(moving_horse_array)

            for j in moving_horse_array:
                stack[new_r][new_c].append(j)
                horse_location_and_directions[j][0], horse_location_and_directions[j][1] = new_r, new_c

            if len(stack[new_r][new_c]) >= 4:
                return turn_count

        turn_count += 1

    return -1




print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))