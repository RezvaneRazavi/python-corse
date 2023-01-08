import random

user_mistakes = 0

words_bank = ["tree", "book", "pink", "life", "freinds"]
true_chars = []
false_chars = []

x = random.randint(0, len(words_bank)-1)
word = words_bank[x]
word = word.lower()
print(word)

#word - random.choice(words_bank)

while True:
    for i in range(len(word)):
        if word[i] in true_chars:
            print(word[i], end="")
        else:
            print("-", end="")

    user_char = input("\nplease write your guess: ")
    user_char = user_char.lower()

    if user_char in word:
        true_chars.append(user_char)
    else:
        false_chars.append(user_char)
        user_mistakes += 1
    
    print("Number of mistakes: ", user_mistakes)
    
    if len(true_chars) == len(word):
        print("you win🎉")
        break

    elif user_mistakes == 6:
        print("Game Over!")
        break
       
    

