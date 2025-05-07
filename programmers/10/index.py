from collections import Counter
picks = [1, 3, 2]
minerals = 	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

def solution(picks, minerals):
    answer = 0

    if len(minerals) <= sum(picks) * 5:
        n = len(minerals)
    else:
        n = sum(picks) * 5

    new_minerals = [[0, 0, 0] for _ in range((len(minerals) // 5 + 1))]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i // 5][0] += 1
        elif minerals[i] == 'iron':
            new_minerals[i // 5][1] += 1
        elif minerals[i] == 'stone':
            new_minerals[i // 5][2] += 1

    new_minerals.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    while new_minerals:
        mineral = new_minerals.pop(0)
        if picks[0] > 0:
            answer += mineral[0] * 1 + mineral[1] * 1 + mineral[2] * 1
            picks[0] -= 1
        elif picks[1] > 0:
            answer += mineral[0] * 5 + mineral[1] * 1 + mineral[2] * 1
            picks[1] -= 1
        else:
            answer += mineral[0] * 25 + mineral[1] * 5 + mineral[2] * 1
            picks[2] -= 1

    return answer



print('나의 정답 :', solution(picks, minerals), '/ 실제 정답: 12')