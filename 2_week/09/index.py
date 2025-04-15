numbers = [1, 1, 1, 1, 1]
target_number = 3


# 재귀함수로 모든 경우의 수를 구한 후 원하는 값이 몇 개 있는지 알아낸다.
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    total_count = []

    def calculate_count_all_way(array, current_index, current_sum):
        if current_index == len(array):
            total_count.append(current_sum)
            return

        calculate_count_all_way(array, current_index + 1, current_sum + array[current_index])
        calculate_count_all_way(array, current_index + 1, current_sum - array[current_index])


    calculate_count_all_way(array, 0, 0)

    result = 0

    for i in total_count:
        if i == target:
            result += 1

    return result


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!