from collections import deque

def find_oil(c_index, land):
    n = len(land)
    m = len(land[0])

    visited = [[False for _ in range(m)] for _ in range(n)]
    check_point = []

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for index in range(n):
        if land[index][c_index] == 1:
            check_point.append([index, c_index])

    queue = deque(check_point)

    oil_count = 0

    while queue:
        r, c = queue.popleft()

        if not visited[r][c] and land[r][c]:
            visited[r][c] = True
            oil_count += 1

        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc

            if 0 <= new_r < n and 0 <= new_c < m:
                if not visited[new_r][new_c] and land[new_r][new_c] == 1:
                    visited[new_r][new_c] = True
                    queue.append([new_r, new_c])
                    oil_count += 1

    return oil_count


def solution(land):
    max_count = 0

    for index in range(len(land[0])):
        count = find_oil(index, land)
        max_count = max(max_count, count)

    return max_count