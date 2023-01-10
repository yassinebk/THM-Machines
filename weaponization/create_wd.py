import os

seasons = ['Spring', 'spring', 'Summer',
           'summer', 'Fall', 'fall', 'Winter', 'winter']

specialCharacters = ['!', '@', '#', '$']

for season in seasons:
    for year in range(2000, 2023):
        for character in specialCharacters:
            password = season + str(year) + character
            with open('passwordlist.txt', 'a') as passwordlist:
                passwordlist.write(password + os.linesep)
