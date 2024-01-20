from csv import reader
import explore_data_module as ed
import apple_cleaning_data_module as acd
import android_cleaning_data_module as adcd
import apple_analyzing_data_module as aadm
import android_analyzing_data_module as adadm


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

print('Conducting Data Analysis for Apple')
aadm.analyzing_data(clean_apple)
print('\n')

print('Conducting Data Analysis for Android')
adadm.analyzing_data(clean_android)
print('\n')

print('Finished Running')