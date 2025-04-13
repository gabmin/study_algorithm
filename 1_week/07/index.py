input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero = 0
    one = 0

    if string[0] == '0':
        one += 1
    elif string[1] == '1':
        zero += 1

    for index in range(len(string) - 1):
        if string[index] != string[index + 1]:
            if string[index] == '0':
                zero += 1
            if string[index] == '1':
                one += 1

    return min(zero, one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)