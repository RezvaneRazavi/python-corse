sum_score = 0
i = 0

while  True:
    score = input("enter student'score: ")

    if score == 'exit':
        break

    sum_score += float(score)
    i += 1

avrage = sum_score / i
print('avrage=', avrage)