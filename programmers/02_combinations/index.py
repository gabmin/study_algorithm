from itertools import combinations


def solution(n, q, ans):
    all_case_arr = list(combinations(range(1, 10 + 1), 5))

    answer = 0
    for case in all_case_arr:
        is_valid = True
        for index in range(len(ans)):
            if len(set(case) & set(q[index])) != ans[index]:
                is_valid = False
                break
        if is_valid:
            answer += 1

    return answer

# 간추린 버전
# def solution(n, q, ans):
#     possible_codes = combinations(range(1, n + 1), 5)
#     count = 0
#
#     for code in possible_codes:
#         if all(len(set(code) & set(q[i])) == ans[i] for i in range(len(q))):
#             count += 1
#
#     return count