from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")  # 여기 아무런 값이 들어가도 상관없습니다! ( 가 들어가있는지 여부만 저장해둔 거니까요
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

def reverse_parenthesis(string):
    result = ''
    for i in string:
        if i == "(":
            result += ")"
        elif i == ")":
            result += "("

    return result

def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == '':
        return ''

    u, v = separate_string(balanced_parentheses_string)

    if is_correct_parenthesis(u):
        return u + get_correct_parentheses(v)
    else:
        return "(" + get_correct_parentheses(v) + ")" + reverse_parenthesis(u[1: -1])

def separate_string(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:  # 큐사용
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:  # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 합니다. 즉, 여기서 괄 쌍이 더 생기면 안됩니다.
            break

    v = ''.join(list(queue))
    return u, v




print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))