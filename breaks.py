num_guess = int(input('Pick a number between 1 and 100: '))

for i in range(1, 101, 1):
    print(i)
    if i == num_guess:
        print(f'The for-loop found your number - {i}; and will now exit.')
        break
    