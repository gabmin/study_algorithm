def josephus_problem(n, k):
    arr = list(range(1, n + 1))
    now_index = k - 1
    answer = []

    while arr:
        target = arr.pop(now_index)
        answer.append(target)
        if len(arr) != 0:
            now_index = (now_index + k - 11) % len(arr) # 일정 범위를 계속 순회해야하는 경우

    return answer


print(josephus_problem(7, 3)) # <3, 6, 2, 7, 5, 1, 4>