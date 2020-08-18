feeling_good = input('Feeling Good?')

if feeling_good == 'y':
    print('Bye')

elif feeling_good == 'n':
    having_headache = input('Have you been having headache? :')

    if having_headache == 'no':
        print('Drink Water!!')

    elif having_headache == 'y':
        stressed_lately = input('Have you been stressed lately? :')

        if stressed_lately == 'y':
            print('Have some rest')

        elif stressed_lately == 'n':
            fever = input('Have you been feverish? : ')

            if fever == 'y':
                print('Call NCDC!!')

        elif fever == 'n':
            print("Sorry can't help you now.!")
