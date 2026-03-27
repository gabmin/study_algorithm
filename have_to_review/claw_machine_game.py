# 프로그래머스 카카오 인턴쉽 인형뽑기게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

board_map = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]

move_map = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    result = 0
    n = len(board)

    stack = []

    for move in moves:
        target = 0

        for i in range(n):
            if board[i][move - 1] != 0:
                target = board[i][move - 1]
                board[i][move - 1] = 0
                break

        if target == 0:
            continue

        if len(stack) == 0:
            stack.append(target)
            continue

        if stack[-1] == target:
            stack.pop()
            result += 2
        else:
            stack.append(target)

    return result


print("정답: 4", solution(board_map, move_map))