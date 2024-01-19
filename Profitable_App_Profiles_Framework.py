from csv import reader
import explore_data_module as ed
import apple_cleaning_data_module as acd
import android_cleaning_data_module as adcd


directory = 'C:\\Personal Projects\\Dataquest\\Python Project\\Apple and Google Apps\\'

apple   = list(reader(open(directory + 'AppleStore.csv')))
android = list(reader(open(directory + 'GooglePlayStore.csv')))

print('Result of Quick Exploration')
ed.explore_data('Apple', apple)
ed.explore_data('Android', android)
print('\n')

print('Cleaning Data for Apple')
clean_apple   = acd.cleaning_data(apple)
print('\n')

print('Cleaning Data for Android')
clean_android = adcd.cleaning_data(android)
print('\n')

print(len(clean_apple))
print(len(clean_android))

print('Finished Running')