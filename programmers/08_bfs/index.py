from collections import deque

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

def solution(board):
    n = len(board)
    m = len(board[0])

    visited = [[False] * m for _ in range(n)]
    start_point = []
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_point = [i, j]

    queue = deque([[start_point[0], start_point[1], 0]])
    visited[start_point[0]][start_point[1]] = True

    while queue:
        r, c, cnt = queue.popleft()

        if board[r][c] == 'G':
            return cnt

        for dx, dy in direction:
            new_r = r
            new_c = c

            while 0 <= new_r + dx < n and 0 <= new_c + dy < m and board[new_r + dx][new_c + dy] != 'D':
                new_r += dx
                new_c += dy

            if not visited[new_r][new_c]:
                visited[new_r][new_c] = True
                queue.append([new_r, new_c, cnt + 1])

    return -1


print(solution(board))