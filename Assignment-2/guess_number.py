import random

sum = 0
computer_number = random.randint(10, 40)

while True:
    sum += 1
    user_number = int(input('enter guess number? '))

    if computer_number == user_number:
        print('you win🎉')
        break

    elif computer_number > user_number:
        print('go up ⬆')

    elif computer_number <  user_number:
        print('go down ⬇')

print('Number of guesses=', sum)

