import random

while True:
    dice = random.randint(1, 6)
    print(dice)
    if dice != 6:
        choice = input('again? yes/no= ')
        if choice == 'no':
            print('by!')
            break
    elif dice == 6:
        print('oOps 6, try again')


