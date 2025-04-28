# from collections import deque
#
# def find_oil(c_index, land):
#     n = len(land)
#     m = len(land[0])
#
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     check_point = []
#
#     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#
#     for index in range(n):
#         if land[index][c_index] == 1:
#             check_point.append([index, c_index])
#
#     queue = deque(check_point)
#
#     oil_count = 0
#
#     while queue:
#         r, c = queue.popleft()
#
#         if not visited[r][c] and land[r][c]:
#             visited[r][c] = True
#             oil_count += 1
#
#         for dr, dc in directions:
#             new_r = r + dr
#             new_c = c + dc
#
#             if 0 <= new_r < n and 0 <= new_c < m:
#                 if not visited[new_r][new_c] and land[new_r][new_c] == 1:
#                     visited[new_r][new_c] = True
#                     queue.append([new_r, new_c])
#                     oil_count += 1
#
#     return oil_count
#
#
# def solution(land):
#     max_count = 0
#
#     for index in range(len(land[0])):
#         count = find_oil(index, land)
#         max_count = max(max_count, count)
#
#     return max_count

#### 성능 개선 버전

from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]
    group_id = [[-1] * m for _ in range(n)]  # 석유 덩어리 그룹 번호 저장
    group_info = dict()  # 그룹별 (석유량, 열들의 집합) 저장
    group_idx = 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                group_id[i][j] = group_idx

                oil_count = 1
                columns = set([j])

                while queue:
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                                group_id[nr][nc] = group_idx
                                oil_count += 1
                                columns.add(nc)

                group_info[group_idx] = (oil_count, columns)
                group_idx += 1

    max_oil = 0

    for col in range(m):
        seen = set()
        oil_sum = 0
        for idx, (oil_count, columns) in group_info.items():
            if col in columns and idx not in seen:
                oil_sum += oil_count
                seen.add(idx)
        max_oil = max(max_oil, oil_sum)

    return max_oil
