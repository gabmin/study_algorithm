# 프로그래머스 카카오 방금 그곡
# https://school.programmers.co.kr/learn/courses/30/lessons/17683
from statsmodels.graphics.tukeyplot import results

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def convert_info(info):
    return info.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b').replace('E#', 'e')

def solution(m, musicinfos):
    new_m = convert_info(m)

    results = []

    for i in musicinfos:
        start, end, title, melody = i.split(',')
        start_hour, start_minute = map(int, start.split(':'))
        end_hour, end_minute = map(int, end.split(':'))

        new_melody = convert_info(melody)
        play_time = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)

        result = ""
        for time in range(play_time):

            index = time % len(new_melody)
            result += new_melody[index]

        if new_m in result:
            results.append([title, play_time])

    if len(results) == 0:
        return "(None)"
    else:
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        return sorted_results[0][0]



print(solution(m, musicinfos)) # "HELLO" 가 출력되어야 합니다.

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

print(solution(m, musicinfos)) # "FOO"