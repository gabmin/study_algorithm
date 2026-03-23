# 백준 극장좌석
# https://www.acmicpc.net/problem/2302

seat_count = 9
vip_seat_array = [4, 7]

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
# vip = [int(line) for line in sys.stdin]

memo = {
    0: 1,
    1: 1,
    2: 2,
}

def get_count(n):
    if n in memo:
        return memo[n]

    value = get_count(n - 1) + get_count(n - 2)
    memo[n] = value
    return value

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    result = 1
    current_index = 0

    for i in fixed_seat_array:
        target_index = i - 1
        result *= get_count(target_index - current_index)
        current_index = target_index + 1

    result *= get_count(total_count - current_index)

    return result

# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))