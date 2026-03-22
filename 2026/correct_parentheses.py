# 프로그래머스 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for i in s:
        stack.append(i)

        if len(stack) >= 2 and stack[-2] == "(" and stack[-1] == ")":
            stack.pop()
            stack.pop()

    return len(stack) == 0

print("정답 = True / 현재 풀이 값 = ", solution("(())"))
print("정답 = False / 현재 풀이 값 = ", solution(")"))
print("정답 = False / 현재 풀이 값 = ", solution("((())))"))
print("정답 = False / 현재 풀이 값 = ", solution("())()"))
print("정답 = False / 현재 풀이 값 = ", solution("((())"))