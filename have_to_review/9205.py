# 백준 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205

from collections import deque
# import sys
# input = sys.stdin.readline
#
# t = int(input())
# test_case = []
# for _ in range(t):
#     n = int(input())
#
#     case = []
#
#     for _ in range(n + 2):
#         case.append(list(map(int, input().split())))
#
#     test_case.append(case)
#

t = 2
test_case = [
    [
        [0, 0],
        [1000, 0],
        [1000, 1000],
        [2000, 1000],
    ],
    [
        [0, 0],
        [1000, 0],
        [2000, 1000],
        [2000, 2000],
    ],
]

def reachable(a, b, case):
    return abs(case[a][0] - case[b][0]) + abs(case[a][1] - case[b][1]) <= 1000


def solution(test_case):
    for case in test_case:

        visited = [False] * len(case)
        queue = deque([0])
        visited[0] = True

        while queue:
            cur = queue.popleft()
            for i in range(len(case)):
                if not visited[i] and reachable(cur, i, case):
                    visited[i] = True
                    queue.append(i)

        print('happy' if visited[-1] else 'sad')

solution(test_case)

