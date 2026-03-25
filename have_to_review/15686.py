# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# map = [list(map(int, input().split())) for _ in range(n)]

from itertools import combinations

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

def calculate_distance(store_list, city_map):
    result = 0

    for i in range(len(city_map)):
        for j in range(len(city_map[i])):
            if city_map[i][j] == 1:
                # 해당 집
                chicken_d_list = []
                for store in store_list:
                    r, c = store
                    distance = abs(i - r) + abs(j - c)
                    chicken_d_list.append(distance)

                result += min(chicken_d_list)

    return result


def get_min_city_chicken_distance(n, m, city_map):
    chicken_store = []

    for i in range(len(city_map)):
        for j in range(len(city_map[i])):
            if city_map[i][j] == 2:
                chicken_store.append((i, j))

    check_list = list(combinations(chicken_store, m))

    result = []
    for comb in check_list:
        d = calculate_distance(list(comb), city_map)

        result.append(d)
    return min(result)


# 출력
print("정답 = 5 / 현재 풀이 값 = ", get_min_city_chicken_distance(n, m, city_map))

city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))