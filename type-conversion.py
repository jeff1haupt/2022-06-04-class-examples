while True:
    try:
        entered_age = input('How old are you (in numeric form)? ')
        entered_age = int(entered_age) # here is the type conversion
        if entered_age >= 18:
            print('You are old enough to vote!')
        else:
            print(f'You have to wait {18-entered_age} more year(s) until you can vote.')
        break
    except ValueError:
        print('Please use integer values only')