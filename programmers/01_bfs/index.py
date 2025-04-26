from collections import deque

# 내 문제 풀이
# import copy
#
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
#
# def is_accessible_container(r, c, storage, visited):
#     n = len(storage)
#     m = len(storage[0])
#
#     visited[r][c] = True
#
#     for i in range(4):
#         new_r = r + dr[i]
#         new_c = c + dc[i]
#
#         if r == 0 or r == n - 1 or c == 0 or c == m - 1:
#             return True
#         elif storage[new_r][new_c] == '0' and not visited[new_r][new_c] and is_accessible_container(new_r, new_c,
#                                                                                                     storage, visited):
#             return True
#
#     return False
#
#
# def solution(storage, requests):
#     for index in range(len(storage)):
#         storage[index] = list(storage[index])
#
#     n = len(storage)
#     m = len(storage[0])
#
#     for alpha in requests:
#         copy_storage = copy.deepcopy(storage)
#         if len(alpha) == 1:
#             for r in range(n):
#                 for c in range(m):
#                     visited = [[False] * m for _ in range(n)]
#                     if copy_storage[r][c] == alpha and is_accessible_container(r, c, copy_storage, visited):
#                         storage[r][c] = '0'
#         else:
#             for r in range(n):
#                 for c in range(m):
#                     if storage[r][c] == alpha[0]:
#                         storage[r][c] = '0'
#
#     total_count = 0
#
#     for r in range(n):
#         for c in range(m):
#             if storage[r][c] != '0':
#                 total_count += 1
#
#     return total_count

def solution(warehouse, requests):
    n = len(warehouse)
    m = len(warehouse[0])
    warehouse = [list(row) for row in warehouse]

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    def bfs():
        visited = [[False]*m for _ in range(n)]
        queue = deque()

        # 해당 i, j 가 외부로 빠저나갈 수 있는지에 대한 값을 visited로 return 함
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and warehouse[i][j] == '.':
                    visited[i][j] = True
                    queue.append((i,j))

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and warehouse[nx][ny] == '.':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        return visited

    for req in requests:
        if len(req) == 1:  # 지게차
            visited = bfs()
            for i in range(n):
                for j in range(m):
                    # 원하는 알파벳이랑 같고 밖으로 빠져나갈 수 있는 곳이라면 .으로 변경
                    if warehouse[i][j] == req and visited[i][j]:
                        warehouse[i][j] = '.'
        else:  # 크레인
            for i in range(n):
                for j in range(m):
                    if warehouse[i][j] == req[0]:
                        warehouse[i][j] = '.'

    # 남은 컨테이너 수 계산
    return sum(row.count('.') for row in warehouse)
