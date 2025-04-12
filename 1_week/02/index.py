def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26

    for word in string:
        if not word.isalpha():
            continue
        target_index = ord(word) - ord('a')
        alphabet_array[target_index] += 1

    max_index = 0
    max_count = 0

    for index in range(len(alphabet_array)):
        if alphabet_array[index] > max_count:
            max_count = alphabet_array[index]
            max_index = index
    return chr(max_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))