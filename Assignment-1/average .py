name = input('please enter name family: ').split()

Number = int(input('How many lessons?'))

score1 = float(input("enter Math score: "))
score2 = float(input("enter Programming score: "))
score3 = float(input("enter Physics score: "))

average = (score1 + score2 + score3) / Number

if average >= 17:
    result = 'Great'

if 17 > average >= 12:
    result = 'Normal'

if average < 12:
    result = 'Fail'


print(average, result)
