# 백준 2048
# https://www.acmicpc.net/problem/12100

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]

n = 3
board = [
    [2, 2, 2],
    [4, 4, 4],
    [8, 8, 8]
]

def merge_line(line):
    nums = [x for x in line if x != 0]
    merged = []
    index = 0

    while index < len(nums):
        if index + 1 < len(nums) and nums[index] == nums[index + 1]:
            merged.append(nums[index] * 2)
            index += 2
        else:
            merged.append(nums[index])
            index += 1

    merged += [0] * (len(line) - len(merged))
    return merged

def move(board, direction):
    # 왼쪽
    if direction == 0:
        return [merge_line(board[r]) for r in range(n)]
    # 오른쪽
    elif direction == 1:
        return [merge_line(board[r][::-1])[::-1] for r in range(n)]
    # 위
    elif direction == 2:
        transformed = [[board[c][r] for c in range(n)] for r in range(n)]
        merged = [merge_line(transformed[r]) for r in range(n)]
        return [[merged[r][c] for c in range(n)] for r in range(n)]
    # 아래
    else:
        transformed = [[board[c][r] for c in range(n)] for r in range(n)]
        merged = [merge_line(transformed[r][::-1])[::-1] for r in range(n)]
        return [[merged[r][c] for c in range(n)] for r in range(n)]

answer = 0

def dfs(board, count):
    global answer


    if count == 5:
        for row in board:
            answer = max(answer, max(row))
        return

    for i in range(4):
        new_board = move(board, i)
        dfs(new_board, count + 1)

dfs(board, 0)

print(answer)


