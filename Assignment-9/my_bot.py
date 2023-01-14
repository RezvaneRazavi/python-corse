import telebot
import random
from telebot import types
from gtts import gTTS
import qrcode
from khayyam import JalaliDate, JalaliDatetime
from datetime import date

my_keyboard = types.ReplyKeyboardMarkup(row_width = 3, resize_keyboard= True)
key1 = types.KeyboardButton("/game")
key2 = types.KeyboardButton("/age")
key3 = types.KeyboardButton("/voice")
key4 = types.KeyboardButton("/max")
key5 = types.KeyboardButton("/argmax")
key6 = types.KeyboardButton("/qrcode")
key6 = types.KeyboardButton("/help")


my_keyboard.add(key1, key2, key3, key4, key5, key6)

game_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1)
key_game = telebot.types.KeyboardButton("/new_game")
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
    birth = bot.send_message(message.chat.id,"تاریخ تولد را وارد نمایید:\n  (با فرمت: روز/ماه/سال)  ") 
    bot.register_next_step_handler(birth, days)

def days(message):   
   birth_date_list = (message.text).split("/")
   year = birth_date_list[0]
   month = birth_date_list[1]
   day = birth_date_list[2]
   year = int(year)
   month = int(month)
   day = int(day)
   cal_day = JalaliDate.today() - JalaliDate(year,month,day) 
   bot.send_message(message.chat.id, cal_day)
   bot.register_next_step_handler(date, days )

@bot.message_handler(commands=['voice'])
def voice(message):
    user_txt = bot.send_message(message.chat.id,"type english sentence: " )
    bot.register_next_step_handler(user_txt, voice_maker)

def voice_maker(message):
    audio = gTTS(text = message.text, lang = "en", slow = False)
    audio.save("audio.mp3")
    audio_file = open("audio.mp3", "rb")
    bot.send_voice(message.chat.id, audio_file)

@bot.message_handler(commands=['max'])
def max(message):
    user_numbers = bot.send_message(message.chat.id, "اعداد خود را با جداسازی ویرگول وارد نمایید")
    bot.register_next_step_handler(user_numbers, max_finder)

def  max_finder(message):
    numbers = message.text.split(",")
    maximum = 0
    for i in range (len(numbers)):
        if int(numbers[i]) > maximum:
            maximum = int(numbers[i])
    bot.send_message(message.chat.id, str(maximum) + "is large number")

@bot.message_handler(commands=['argmax'])
def argmax(message):
    user_numbers = bot.send_message(message.chat.id, "اعداد خود را با جداسازی ویرگول وارد نمایید")
    bot.register_next_step_handler(user_numbers, index_finder)

def index_finder(message):
    numbers = message.text.split(",")
    maximum = 0
    index = 0
    for i in range (len(numbers)):
        if int(numbers[i]) > maximum:
            maximum = int(numbers[i])
            index = i + 1
    bot.send_message(message.chat.id, "position of " + str(maximum) + " is: " + str(index))

@bot.message_handler(commands=['qrcode'])
def QRcode(message):
    user_txt = bot.send_message(message.chat.id, "Type your english sentence")
    bot.register_next_step_handler(user_txt, QRcode_maker)

def QRcode_maker(message):
    user_qrcode = qrcode.make(message.text)
    user_qrcode.save("QR.jpg")
    QR_file = open("QR.jpg", "rb")
    bot.send_photo(message.chat.id, QR_file)







@bot.message_handler(func= lambda m:True)
def echo_all(message):
    if message.text == "سلام":
        bot.send_message(message.chat.id , "سلام عزیزم")
    else:
        bot.send_message(message.chat.id , "نمیفهمم چی میگی؟", reply_markup= my_keyboard)


bot.infinity_polling()