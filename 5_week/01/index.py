from collections import deque

c = 11
b = 2

def catch_me(cony_loc, brown_loc):
    queue = deque()
    queue.append(brown_loc)

    time = 0

    while cony_loc <= 200000:
        cony_loc += time

        if cony_loc in queue:
            break

        for i in range(len(queue)):
            target = queue.popleft()

            new_position = target - 1
            if 0 < new_position <= 200000:
                queue.append(new_position)

            new_position = target + 1
            if 0 < new_position <= 200000:
                queue.append(new_position)

            new_position = target * 2
            if 0 < new_position <= 200000:
                queue.append(new_position)

        time += 1

    return time


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))