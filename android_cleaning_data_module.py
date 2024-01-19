def remove_incomplete_data(dataset):
    num_of_incomplete   = 0
    cleaned_data        = []

    for row in dataset:
        if len(row) != 13:
            num_of_incomplete += 1
            continue
        else:
            cleaned_data.append([row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[9]])

    print('Number of Incomplete Rows Removed for Android: ', num_of_incomplete)
    return cleaned_data

def remove_non_eng_app(dataset):
    num_of_non_eng_apps = []
    cleaned_data        = []

    for row in dataset:
        app_name    = row[0].strip()
        category    = row[1].strip()
        rating      = row[2].strip()
        review      = row[3].strip()
        install     = row[4].strip()
        price_type  = row[5].strip()
        price       = row[6].strip()
        genre       = row[7].strip()

        # Removing Non-English Apps
        count_to_remove_non_eng_app = 0
        for letter in app_name:
            if ord(letter) > 127:
                count_to_remove_non_eng_app += 1
        if count_to_remove_non_eng_app >= 3:
            num_of_non_eng_apps.append(app_name)
            continue

        cleaned_data.append([app_name, category, rating, review, install, price_type, price, genre])
    print('Number of Non-English Apps Removed for Android: ', len(num_of_non_eng_apps))
    return cleaned_data

def remove_non_free(dataset):
    num_of_non_free_apps    = []
    cleaned_data            = []

    for row in dataset:
        app_name    = row[0].strip()
        category    = row[1].strip()
        rating      = row[2].strip()
        review      = row[3].strip()
        install     = row[4].strip()
        price_type  = row[5].strip()
        price       = row[6].strip()
        genre       = row[7].strip()

        # Removing Non-Free Apps
        if price_type.lower() == 'free':
            price = float(price)
        else:
            num_of_non_free_apps.append(app_name)
            continue

        cleaned_data.append([app_name, category, rating, review, install, price_type, price, genre])

    print('Number of Non-Free Apps Removed for Android: ', len(num_of_non_free_apps))
    return cleaned_data

def remove_duplicated(dataset):
    app_with_rating         =   {}
    duplicated_app_number   =   0
    cleaned_data            = []

    for row in dataset:
        app_name    = row[0].strip()
        category    = row[1].strip()
        rating      = row[2].strip()
        review      = row[3].strip()
        install     = row[4].strip()
        price_type  = row[5].strip()
        price       = row[6]
        genre       = row[7].strip()

        # Removing Duplicated Apps With Higher User Rating
        if app_name not in app_with_rating:
            app_with_rating[app_name] = review

        elif app_name in app_with_rating:
            if app_with_rating[app_name] >= review:
                duplicated_app_number += 1
                continue
            else:
                app_with_rating[app_name] = review
                for app in cleaned_data:
                    if app[0] == app_name:
                        app[3] = review
                        duplicated_app_number += 1
                        continue

        cleaned_data.append([app_name, category, rating, review, install, price, genre])

    print('Number of Duplicated Apps Removed for Android: ', duplicated_app_number)
    return cleaned_data

def cleaning_data(dataset):
    removing_incomplete = remove_incomplete_data(dataset)
    removing_non_eng    = remove_non_eng_app(removing_incomplete)
    removing_non_free   = remove_non_free(removing_non_eng)
    cleaned_data        = remove_duplicated(removing_non_free)

    return cleaned_data

