from collections import Counter
picks = [1, 3, 2]
minerals = 	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

# 곡갱이를 사용하면 광물 5개를 캐야하므로 5개씩 끊어서 새로운 배열을 만들어줌
# ex) [[3,2,0],[1,1,1]]
# 다이아몬드가 많은 순서대로 정렬을 해준다.
# 정렬된 배열을 다이아몬드 곡갱이부터 사용하면서 피로도를 계산한다.
def solution(picks, minerals):
    answer = 0

    if len(minerals) <= sum(picks) * 5:
        n = len(minerals)
    else:
        n = sum(picks) * 5

    new_minerals = [[0, 0, 0] for _ in range((len(minerals) // 5 + 1))]
    for i in range(n):
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