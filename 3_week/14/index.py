genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    total_count_dict = {}
    index_dict = {}

    for i in range(len(genre_array)):
        if genre_array[i] in total_count_dict:
            total_count_dict[genre_array[i]] += play_array[i]
            index_dict[genre_array[i]].append([i, play_array[i]])
        else:
            total_count_dict[genre_array[i]] = play_array[i]
            index_dict[genre_array[i]] = [[i, play_array[i]]]

    sorted_total_array = sorted(total_count_dict.items(), key=lambda item: item[1], reverse=True)

    result = []
    for genre, play in sorted_total_array:
        sorted_index_array = sorted(index_dict[genre], key=lambda item:item[1], reverse=True)

        add_count = 0
        for index, data in sorted_index_array:
            if add_count >= 2:
                break
            result.append(index)
            add_count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))