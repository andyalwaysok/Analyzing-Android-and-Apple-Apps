def sorting_dictionary(dictionary):
    sorting_list = []
    for key, value in dictionary.items():
        sorting_list.append([value, key])

    sorted_list = sorted(sorting_list, reverse = True)
    return sorted_list

def freq_table(dataset):
    genre_dict  =   {}
    for row in dataset:
        category               =   row[1].strip()

        if category in genre_dict:
            genre_dict[category] += 1
        else:
            genre_dict[category] = 1

    for genre, value in genre_dict.items():
        new_value = (value / len(dataset)) * 100
        genre_dict[genre] = round(new_value, 2)

    sorting_process = sorting_dictionary(genre_dict)
    return sorting_process

def analyzing_data(dataset):
    analyzing = freq_table(dataset)
    print('The Top 3 Category/Genre for Android is: ')
    print(analyzing[0][1], 'with percentage of ', analyzing[0][0], '%')
    print(analyzing[1][1], 'with percentage of ', analyzing[1][0], '%')
    print(analyzing[2][1], 'with percentage of ', analyzing[2][0], '%')

