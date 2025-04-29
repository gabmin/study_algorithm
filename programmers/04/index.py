from itertools import combinations

points = [[3, 2], [6, 4], [4, 7], [1, 4]]
routes = [[4, 2], [1, 3], [4, 2], [4, 3]]

def move_point(point):
    start_point, end_point = point
    new_point_x = start_point[0]
    new_point_y = start_point[1]

    if start_point[0] != end_point[0]:
        if end_point[0] > start_point[0]:
            new_point_x += 1
        else:
            new_point_x -= 1
    else:
        if end_point[1] > start_point[1]:
            new_point_y += 1
        else:
            new_point_y -= 1

    return [new_point_x, new_point_y]

def solution(points, routes):
    moved_point = []

    for route in routes:
        for i in range(len(route) - 1):
            start_point = points[route[i] - 1]
            end_point = points[route[i + 1] - 1]
            moved_point.append([start_point, end_point])

    collision = 0

    while any(i[0] != i[1] for i in moved_point):
        for index in range(len(moved_point)):
            if moved_point[index][0] == moved_point[index][1]:
                continue

            moved_point[index][0] = move_point(moved_point[index])

        now_point_arr = [i[0] for i in moved_point]
        print(now_point_arr)

        for a, b in list(combinations(now_point_arr, 2)):
            if a == b:
                collision += 1


    return collision


print('정답: result: 1 // 내 결과 값 :', solution(points, routes))