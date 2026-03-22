from collections import defaultdict

def solution(genre_array, play_array):
    genre_dict = defaultdict(int)
    info_dict = defaultdict(list)
    result = []


    for i in range(len(genre_array)):
        genre_dict[genre_array[i]] += play_array[i]
        info_dict[genre_array[i]].append((i, play_array[i]))

    sorted_genre_dict = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)


    for genre, total_play in sorted_genre_dict:
        sorted_info_dict = sorted(info_dict[genre], key=lambda x: x[1], reverse=True)

        count = 0
        for index, play in sorted_info_dict:
            if count >= 2:
                break

            result.append(index)
            count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", solution(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))