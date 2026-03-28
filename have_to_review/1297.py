# 백준 순바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())

n, k = 5, 17

def solution(n, k):
    if n == k:
        return 0

    queue = deque([[n, 0]])
    visited = set()
    visited.add(n)

    while queue:
        position, time = queue.popleft()

        for next_pos in [position + 1, position - 1, position * 2]:
            if 0 <= next_pos <= 100000 and next_pos not in visited:
                if next_pos == k:
                    return time + 1
                visited.add(next_pos)
                queue.append([next_pos, time + 1])

print(solution(n, k))