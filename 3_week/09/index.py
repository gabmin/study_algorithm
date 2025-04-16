prices = [1, 2, 3, 2, 3]

from collections import deque

# O(N^2)
def get_price_not_fall_periods(prices):
    queue = deque(prices)

    answer = []
    while queue:
        target = queue.popleft()

        count = 0
        for i in queue:

            if target <= i:
                count += 1
            else:
                count += 1
                break

        answer.append(count)

    return answer


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))