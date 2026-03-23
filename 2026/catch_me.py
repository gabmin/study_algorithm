from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    queue = deque()
    queue.append(brown_loc)
    time = 1
    acc = 1
    while cony_loc <= 200000:
        cony_loc = cony_loc + acc

        acc += 1

        temp = []
        while queue:
            loc = queue.popleft()

            new_loc1 = loc + 1
            new_loc2 = loc - 1
            new_loc3 = loc * 2

            if 0 <= new_loc1 <= 200000:
                temp.append(new_loc1)
            if 0 <= new_loc2 <= 200000:
                temp.append(new_loc2)
            if 0 <= new_loc3 <= 200000:
                temp.append(new_loc3)

        queue = deque(set(temp))

        if cony_loc in queue:
            break

        time += 1

    return time

print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))