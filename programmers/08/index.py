from collections import deque

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

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
            new_r = r + d[0]
            new_c = c + d[1]

            while board[new_r][new_c] != 'D':
                if n < new_r < 0 and m < new_c < 0:
                    break

                if board[new_r][new_c] != 'D' and not [new_r, new_c] in visited:
                    queue.append([r, c])
                    answer += 1

    return answer


print(solution(board))