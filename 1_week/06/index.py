input = 20


def find_prime_list_under_number(number):
    answer = []

    for num in range(number + 1):
        if num == 1:
            continue
        if num == 2 or num == 3:
            answer.append(num)
        if num % 2 != 0 and num % 3 != 0:
            answer.append(num)

    print(answer)
    return answer


result = find_prime_list_under_number(input)
print(result)