array = [5, 3, 2 ,1 ,6, 8 ,7, 4]

# O(NlogN)
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return merge(left_array, right_array)

# O(N)
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index < len(array1):
        result += array1[array1_index:]
    else:
        result += array2[array2_index:]

    return result


print(merge_sort(array))