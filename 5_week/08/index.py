def convert_sharp(melody):
    return melody.replace("C#", "c").replace("D#", "d")\
                 .replace("F#", "f").replace("G#", "g").replace("A#", "a")

def solution(m, musicinfos):
    m = convert_sharp(m)
    result = []

    for info in musicinfos:
        start, end, title, melody = info.split(",")
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))

        duration = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        melody = convert_sharp(melody)

        # 재생된 음악 생성
        played = (melody * (duration // len(melody) + 1))[:duration]

        if m in played:
            result.append((duration, title))

    if not result:
        return "(None)"
    else:
        return sorted(result, key=lambda x: -x[0])[0][1]
