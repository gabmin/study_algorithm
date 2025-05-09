citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort()

    n = len(citations)
    for i in range(n):

        if citations[i] >= n - i:
            return n - i
    return 0



print('나의 정답 :', solution(citations), '/ 실제 정답: 3')
