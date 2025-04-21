input = "abcabcabcabcdededededede"

def string_compression(string):

    half_length = len(string) // 2

    result = len(string)

    for i in range(1, half_length + 1):
        new_arr = [
            string[j: j + i] for j in range(0, len(string), i)
        ]

        new_string = ""
        count = 1
        for i in range(0, len(new_arr) - 1):
            cur, next = new_arr[i], new_arr[i + 1]

            if cur == next:
                count += 1
                if i + 1 == len(new_arr) - 1:
                    new_string += f"{count}{cur}"
            else:
                if count == 1:
                    new_string += cur
                else:
                    new_string += f"{count}{cur}"
                count = 1

        if count == 1:
            new_string += new_arr[-1]

        result_len = len(new_string)

        result = min(result, result_len)

    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))