# 백준 시험 감독
# https://www.acmicpc.net/problem/13458

import math
# import sys
# input = sys.stdin.readline
#
# # 시험장 개수
# n = int(input())
# # 응시자 수
# a = list(map(int, input().split()))
# # 감독관 감시 수
# b, c = map(int, input().split())

n = 3
a = [3, 4, 5]
b, c = 2, 2

def solution(n, a, b, c):
    result = 0

    for i in a:
        i = i - b
        result += 1

        if i > 0:
            result += math.ceil(i / c)

    return result



print("정답: 7", "풀이:", solution(n, a, b, c))

n = 5
a = [1000000, 1000000, 1000000, 1000000, 1000000]
b, c = 5, 7

print("정답: 714290", "풀이:", solution(n, a, b, c))