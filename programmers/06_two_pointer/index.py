# 투 포인터

def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    total = sequence[0]
    answer = [0, n-1]

    while start < n and end < n:
        if total == k:
            # 최적의 범위를 구하기 위해 answer에 저장 후 계속 진행
            # ex) k=5, [1,1,1,2] x / [2, 3] o
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
            total -= sequence[start]
            start += 1
        elif total < k:
            end += 1
            if end < n:
                total += sequence[end]
        else:
            total -= sequence[start]
            start += 1

    return answer