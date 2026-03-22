## https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def solution(numbers, target):
    result = []
    answer = 0
    def calculation(array, current_index, current_sum):
        if current_index == len(array):
            result.append(current_sum)
            return
        calculation(array, current_index + 1, current_sum + array[current_index])
        calculation(array, current_index + 1, current_sum - array[current_index])

    calculation(numbers, 0, 0)

    for data in result:
        if data == target:
            answer += 1

    return answer

def solution2(numbers, target):
    stack = [0]
    for num in numbers:
        temp = []
        for data in stack:
            temp.append(data + num)
            temp.append(data - num)

        stack = temp

    return stack.count(target)

print(solution2([4, 1, 2, 1], 4))