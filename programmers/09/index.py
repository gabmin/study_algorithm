targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

def solution(targets):
    sorted_targets = sorted(targets, key=lambda x: x[1])

    count, end = 0, 0
    for s, e in sorted_targets:
        if s >= end:
            count += 1
            end = e
    return count


print('나의 정답 :', solution(targets), '/ 실제 정답: 3')