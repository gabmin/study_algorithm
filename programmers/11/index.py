from collections import deque

maps = ["X591X","X1X5X","X231X", "1XXX1"]

def solution(maps):
    new_maps = []
    for m in maps:
        new_maps.append(list(m))

    m = len(new_maps)
    n = len(new_maps[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited = [[False for _ in range(n)] for _ in range(m)]

    answer = []

    for i in range(m):
        for j in range(n):
            if new_maps[i][j] != 'X' and not visited[i][j]:

                queue = deque([[i, j]])

                count = 0
                while queue:
                    r, c = queue.popleft()
                    visited[r][c] = True

                    if new_maps[r][c] != 'X':
                        count += int(new_maps[r][c])

                    for dx, dy in directions:
                        new_r = r + dx
                        new_c = c + dy

                        if 0 <= new_r < m and 0 <= new_c < n:
                            if new_maps[r][c] != 'X' and not visited[new_r][new_c]:
                                queue.append([new_r, new_c])
                                visited[new_r][new_c] = True

                if count != 0:
                    answer.append(count)

    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer, key=lambda x: x)

print('나의 정답 :', solution(maps), '/ 실제 정답: [1, 1, 27]')