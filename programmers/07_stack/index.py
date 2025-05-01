plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
def convert_time(time):
    hour, minute = time.split(':')

    return int(hour) * 60 + int(minute)

def solution(plans):
    sorted_plans = sorted(plans, key=lambda x: x[1])

    stack = []
    result = []

    for index in range(len(sorted_plans)):
        name, start, playtime = sorted_plans[index]

        if index == len(sorted_plans) - 1:
            result.append(name)

            while stack:
                result.append(stack.pop()[0])
        else:
            diff_time = convert_time(sorted_plans[index + 1][1]) - convert_time(start)

            rest_time = int(playtime) - diff_time

            if rest_time <= 0:
                result.append(name)

                while rest_time < 0:
                    if len(stack) == 0:
                        break

                    todo_name, todo_start, todo_playtime = stack.pop()

                    if todo_playtime + rest_time > 0:
                        stack.append([todo_name, todo_start, int(todo_playtime) + rest_time])
                        rest_time += int(todo_playtime)
                    else:
                        result.append(todo_name)
                        rest_time += int(todo_playtime)
            else:
                stack.append([name, start, rest_time])


    return result

print(solution(plans))