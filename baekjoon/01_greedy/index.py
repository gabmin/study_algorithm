n = 161

def get_sum_position(n):
   return sum(int(i) for i in str(n))

def solution(n):
    x = n // 2
    y = n - x

    while abs(get_sum_position(x) - get_sum_position(y)) > 1:
        x -= 1
        y += 1


    return [x, y]

print('나의 정답 :', solution(n), '/ 실제 정답: 67 94')