def cleaning_data(dataset):
    checking_duplicate      = []
    app_with_rating         = {}
    duplicate_app_list      = []

    num_of_non_eng_apps     = []

    num_of_non_free_apps    = []

    clean_data = []

    for row in dataset:
        id                  =   row[1].strip()
        app_name            =   row[2].strip()
        size                =   row[3].strip()
        currency            =   row[4].strip()
        price               =   row[5].strip()
        rating_count_total  =   row[6].strip()
        user_rating         =   row[8].strip()
        genre               =   row[12].strip()

        if id == 'id':
            continue

        # Removing Non-English Apps
        count_to_remove_non_eng_app = 0
        for letter in app_name:
            if ord(letter) > 127:
                count_to_remove_non_eng_app += 1
        if count_to_remove_non_eng_app > 3:
            num_of_non_eng_apps.append(app_name)
            continue

        # Removing Non-Free Apps
        price = float(price)
        if price != 0.0:
            num_of_non_free_apps.append(app_name)
            continue

        # Removing Duplicated Apps With Higher User Rating
        if app_name not in checking_duplicate:
            app_with_rating[app_name] = rating_count_total
            checking_duplicate.append(app_name)

        elif app_name in checking_duplicate:
            if app_with_rating[app_name] > rating_count_total:
                continue
            else:
                app_with_rating[app_name] = rating_count_total

            duplicate_app_list.append(app_name)

        clean_data.append([id, app_name, size, currency, price, rating_count_total, user_rating, genre])

    print('Number of Non-English Apps Removed for Apple: ', len(num_of_non_eng_apps))
    print('Number of Duplicated Apps Removed for Apple: ', len(duplicate_app_list))
    print('Number of Non-Free Apps Removed for Apple: ', len(num_of_non_free_apps))
    return clean_data