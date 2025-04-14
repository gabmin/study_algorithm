input = "abcba"


def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) == 0:
        return True

    return is_palindrome(string[1: -1])


print(is_palindrome(input))