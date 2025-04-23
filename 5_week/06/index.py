import itertools

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

def get_chicken_distance(h, s):
    result = 0

    for store_r, store_c in s:
        chicken_d = []
        for house_r, house_c in h:
            chicken_d.append(abs(store_r - house_r) + abs(store_c - house_c))

        result += min(chicken_d)

    return result

def get_min_city_chicken_distance(n, m, city_map):
    store_arr = []
    house_arr = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 2:
                store_arr.append([i, j])
            if city_map[i][j] == 1:
                house_arr.append([i, j])

    max_store_list = (list(itertools.combinations(store_arr, m)))

    all_case_count = []
    for case in max_store_list:
        all_case_count.append(get_chicken_distance(case, house_arr))

    return min(all_case_count)



# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


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