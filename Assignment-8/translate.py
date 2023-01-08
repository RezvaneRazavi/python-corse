import gtts
import os

def read_from_file():
    global words_bank
    f = open("Assignment-8/translate.txt", "r")

    #words = []
    # for line in f:
    #     words.append(line)
    # print(words)

    temp = f.read().split("\n")

    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)
    
    f.close()

def show_menu():
    print("1- translate english to persian")
    print("2- translate persian to english")
    print("3- add a new word to database")
    print("4-show txt")
    print("5-exit")

def translate_english_to_persian():
    output = ""
    user_txt = input("enter your english text: ").lower()
    user_sentence = user_txt.split('.')
    
    for sentence in user_sentence:
        user_words = sentence.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word == word["en"]:
                    output = output + word["fa"] + " "
                    break
            else:
                output = output + user_word + " "
            
        output = output + '.'

    print(output)

def translate_persian_to_english():
    output = ""
    user_txt = input("enter your persian txt: ").lower()
    user_sentence = user_txt.split('.')

    for sentence in user_sentence:
        user_words = sentence.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word ==  word['fa']:
                    output = output + word['en'] + " "
                    break
            else:
                output = output + user_word + ' '

        output = output + '.'
    print(output)
    my_voice = gtts.gTTS(output , lang="en", slow = False)
    my_voice.save("Assignment-8/voice.mp3")
    os.system('start Assignment-8\voice.mp3')

def write_to_file():
    en_word = input("enter 'en' word: " ).lower()
    fa_word = input("enter 'fa' word: ").lower()
    for word in words_bank:
        if word['en'] == en_word:
            print('word is exists.')
            break
    else:        
        new_word = {'en': en_word, 'fa': fa_word}
        words_bank.append(new_word)
        f = open("Assignment-8/translate.txt", "a")
        f.write("\n")
        f.write(en_word)
        f.write("\n")
        f.write(fa_word)
        f.close()
        print("successfully add", en_word, ":", fa_word)

read_from_file()
print("welocme to my translate")

while True:
    show_menu()
    choice = int(input("enter your choice: "))
    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        write_to_file()
    elif choice == 4:
        print(words_bank)
    elif choice == 5:
        exit(0)