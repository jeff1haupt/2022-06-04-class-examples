password = 'password123!'

while True:
    user_password = input('Please enter your password: ')
    print(type(user_password))
    if user_password == password:
        break
    else:
        print('Incorrect password entered, try again.')