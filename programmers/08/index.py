from collections import deque

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move_straight(now_position, direction, n, m):
    r, c = now_position
    while board[r][c] != 'D':
        if 0 <= r < n and 0 <= c < m:
            r = r + direction[0]
            c = c + direction[1]
        else: break

    return [r, c]

def solution(board):
    n = len(board)
    m = len(board[0])

    visited = []
    start_point = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_point = [i, j]

    queue = deque([start_point])
    answer = 0

    while queue:
        r, c = queue.popleft()
        visited.append([r, c])

        print(r, c)

        if board[r][c] == 'G':
            break

        for d in direction:
            while 0 <= r < n and 0 <= c < m:
                new_r = r + d[0]
                new_c = c + d[1]

                if board[new_r][new_c] != 'D' and not [new_r, new_c] in visited:
                    queue.append([r, c])
                    answer += 1

    return answer


print(solution(board))