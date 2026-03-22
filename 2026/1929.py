# https://www.acmicpc.net/problem/1929

M = 3
N = 16

def main(m, n):
    for i in range(m, n + 1):
        if i < 2:
            continue
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)

main(M, N)