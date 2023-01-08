import random
import telebot
from telebot import types

my_keyboard = types.ReplyKeyboardMarkup(row_width = 3, resize_keyboard= True)
key1 = types.KeyboardButton("/game")
key2 = types.KeyboardButton("/age")
key3 = types.KeyboardButton("/voice")
key4 = types.KeyboardButton("/max")
key5 = types.KeyboardButton("/argmax")
key6 = types.KeyboardButton("/qrcode")
key6 = types.KeyboardButton("/help")


my_keyboard.add(key1, key2, key3, key4, key5, key6)

game_keyboard = types.ReplyKeyboardMarkup(row_width=1)
key_game = types.KeyboardButton("/new_game")
game_keyboard.add(key_game)


bot = telebot.TeleBot("5808326396:AAEw5GoqiqcclzjiQQTjLoszXG1S3E_pwm0", parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام " + message.from_user.first_name + "خوش اومدی ", reply_markup = my_keyboard)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """
    /start
    Welcome.\n
    /game
    Quess number\n
    /age 
    age calculation \n
    /voice 
    english sentence to voice \n
    /max
    max array \n
    /argmax 
    largest max array \n
    /qrcode
    sentence to QRcode 
    /help
    menue  """)


computer_number = random.randint(10, 40)
@bot.message_handler(commands=['game' , 'new_game'])
def start_game(message):
    mesaage1 = bot.send_message(message.chat.id, "Enter a number between 10 and 40" , reply_markup = game_keyboard )
    bot.register_next_step_handler(mesaage1, play_game )
    
def play_game(message):
        if computer_number == int(message.text):
            mess2 = bot.send_message(message.chat.id , "you win🎉")
            bot.register_next_step_handler(mesaage2, play_game)

        elif computer_number > int(message.text):
            mesaage2 = bot.send_message(message.chat.id , 'go up ⬆', reply_markup = game_keyboard )
            bot.register_next_step_handler(mesaage2, play_game)

        elif computer_number <  int(message.text):
           mess2 = bot.send_message(message.chat.id , 'go down ⬇' , reply_markup = game_keyboard )
           bot.register_next_step_handler(mess2, play_game)
        
        
@bot.message_handler(commands=['age'])
def date_birth(message):
  birth=bot.send_message(message.chat.id,"تاریخ تولد را وارد نمایید:\n  (با فرمت: روز/ماه/سال)  ") 

@bot.message_handler(commands=['voice'])


@bot.message_handler(commands=['max'])


@bot.message_handler(commands=['argmax'])


@bot.message_handler(commands=['qrcode'])

@bot.message_handler(func= lambda m:True)
def echo_all(message):
    if message.text == "سلام":
        bot.send_message(message.chat.id , "سلام عزیزم")
    elif message.text == "خوبی؟":
        bot.send_message(message.chat.id , "خوبم تو چطوری؟")
    # elif message.text == "ی عکس بده":
    #     photo = open("Assignment-8/pic.jpg", 'rb')
    #     bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id , "نمیفهمم چی میگی؟", reply_markup= my_keyboard)


bot.infinity_polling()