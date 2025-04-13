def find_not_repeating_first_character(string):
    occurrence_array = find_max_occurred_alphabet(string)

    result_arr = []

    for index in range(len(occurrence_array)):
        if occurrence_array[index] == 1:
            result_arr.append(chr(index + ord('a')))

    for char in string:
        if char in result_arr:
            return char
    return "_"

def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26

    for word in string:
        if not word.isalpha():
            continue
        target_index = ord(word) - ord('a')
        alphabet_array[target_index] += 1

    return alphabet_array

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))