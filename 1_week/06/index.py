input = 20


def find_prime_list_under_number(number):
    answer = []

    for num in range(2, number + 1):
        for i in answer:
            if num % i == 0:
                break
        else:
            answer.append(num)

    return answer


result = find_prime_list_under_number(input)
print(result)