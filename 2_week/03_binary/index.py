finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 시간 복잡도 : O(log(N))

def is_existing_target_number_binary(target, array):
    min_index = 0
    max_index = len(array) - 1
    center_index = (min_index + max_index) // 2

    while min_index <= max_index:
        if array[center_index] == target:
            return True
        elif array[center_index] < target:
            min_index = center_index + 1
        else:
            max_index = center_index - 1

        center_index = (min_index + max_index) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)