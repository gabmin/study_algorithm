from collections import defaultdict
import math

def solution(lines):
    data = defaultdict(int)

    for log in lines:
        _, time, duration = log.split(" ")
        hour, minute, second = map(float, time.split(":"))

        duration = float(duration.replace("s", ""))

        start, end = second - duration + 0.001, second

        print(start, end)

        start = math.floor(start)
        end = math.floor(end)

        for i in range(start, end):
            data[i] += 1

    print(data.items())

    return 0