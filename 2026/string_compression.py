input = "abcabcabcabcdededededede"

def string_compression(string):
    n = len(string) // 2
    result = len(string)

    for slice_number in range(1, n + 1):
        temp_array = []
        temp_string = ''
        temp_count = 1

        for j in range(0, len(string) + 1, slice_number):
            if len(temp_array) == 0:
                temp_array.append(string[0: j + slice_number])
                continue

            before_target = temp_array.pop()
            current_target = string[j: j + slice_number]

            if before_target == current_target:
                temp_count += 1
            else:
                if temp_count > 1:
                    temp_string += f"{temp_count}{before_target}"
                else:
                    temp_string += before_target

                temp_count = 1

            temp_array.append(current_target)

        rest = len(string) % slice_number
        if rest != 0:
            temp_string += string[-rest:]

        if len(temp_string) < result:
            result = len(temp_string)

    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

# print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
# print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))