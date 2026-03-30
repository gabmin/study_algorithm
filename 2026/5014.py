# 백준 스타트링크
# https://www.acmicpc.net/problem/5014

from collections import deque
# import sys
# input = sys.stdin.readline

# f, s, g, u, d = map(int, input().split())


# 건물의 층수 F
# 스타트링크의 층수 G
# 현재 위치 S

f = 10
s = 1
g = 10
u = 2
d = 1

def solution(f, s, g, u, d):
    queue = deque([[s, 0]])
    visited = [False for _ in range(f + 1)]
    visited[s] = True

    while queue:
        position, count = queue.popleft()

        if position == g:
            return count

        for new_position in [position + u, position - d]:
            if 1 <= new_position <= f and not visited[new_position]:
                queue.append([new_position, count + 1])
                visited[new_position] = True

    return 'use the stairs'

print("정답: 6", "풀이:", solution(f, s, g, u, d))

f = 100
s = 2
g = 1
u = 1
d = 0

print("정답: use the stairs", "풀이:", solution(f, s, g, u, d))
