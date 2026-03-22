# https://www.acmicpc.net/problem/1439
import sys
input = sys.stdin.readline

m = input().strip()

def main(m):
    zero = []
    one = []

    start_index = 0

    for index in range(0, len(m)):

        if index == len(m) - 1 or m[index] != m[index + 1]:
            if m[index] == "0":
                zero.append(m[start_index:index + 1])

            if m[index] == "1":
                one.append(m[start_index:index + 1])

            start_index = index + 1

    return min(len(zero), len(one))

print(main(m))
