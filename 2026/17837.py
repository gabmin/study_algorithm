import sys
input = sys.stdin.readline

n, k = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]
location_info = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    location_info[i][0] -= 1
    location_info[i][1] -= 1

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def back_direction(d):
    if d % 2 != 0:
        return d + 1
    return d - 1

def solution(horse_count, game_map, position):
    n = len(game_map)
    m = len(game_map[0])
    count = 1
    location = [[[] for _ in range(m)] for _ in range(n)]

    for index in range(len(position)):
        r, c, d = position[index]
        location[r][c].append(index + 1)  # 1-based

    while count < 1000:
        for horse_number in range(1, horse_count + 1):
            r, c, d = position[horse_number - 1]

            new_r, new_c = r + dr[d - 1], c + dc[d - 1]
            new_d = d

            if not (0 <= new_r < n and 0 <= new_c < m) or game_map[new_r][new_c] == 2:
                new_d = back_direction(new_d)
                position[horse_number - 1][2] = new_d
                new_r, new_c = r + dr[new_d - 1], c + dc[new_d - 1]

                if not (0 <= new_r < n and 0 <= new_c < m) or game_map[new_r][new_c] == 2:
                    continue

            next_array = []
            for i in range(len(location[r][c])):
                if location[r][c][i] == horse_number:
                    previous = location[r][c][:i]
                    next_array = location[r][c][i:]
                    location[r][c] = previous
                    break  # 찾으면 바로 종료

            if game_map[new_r][new_c] == 1:
                next_array = next_array[::-1]  # 뒤집기

            for j in next_array:
                location[new_r][new_c].append(j)
                position[j - 1][0] = new_r  # 1-based 보정
                position[j - 1][1] = new_c

            position[horse_number - 1][2] = new_d

            if len(location[new_r][new_c]) >= 4:
                return count

        count += 1

    return -1

print(solution(k, game_map, location_info))