def check_result(diffs, times, limit, level):
    count = 0

    for index in range(len(diffs)):
        if diffs[index] <= level:
            count += times[index]
        else:
            repeat = diffs[index] - level
            count += (times[index] + times[index - 1]) * repeat + times[index]

    if count <= limit:
        return True
    else:
        return False


def solution(diffs, times, limit):
    start = 0
    end = max(diffs)

    while start <= end:
        half = (start + end) // 2

        if check_result(diffs, times, limit, half):
            end = half - 1
        else:
            start = half + 1

    return start
