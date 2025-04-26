from collections import deque

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
