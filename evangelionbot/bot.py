import telebot
import config
import random
from telebot import types
bot = telebot.TeleBot(config.TOKEN)
asuka = ["Asuka/1.webp", "Asuka/2.webp", "Asuka/3.webp", "Asuka/4.webp", "Asuka/5.webp", "Asuka/6.webp", "Asuka/7.webp",
"Asuka/8.webp", "Asuka/9.webp", "Asuka/10.webp", "Asuka/11.webp", "Asuka/12.webp", "Asuka/13.webp", "Asuka/14.webp"]
rey = ["Rey/1.webp", "Rey/2.webp", "Rey/3.webp", "Rey/4.webp", "Rey/5.webp", "Rey/6.webp", "Rey/7.webp",
         "Rey/8.webp", "Rey/9.webp", "Rey/10.webp", "Rey/11.webp", "Rey/12.webp", "Rey/13.webp", "Rey/14.webp"]
misato = ["Misato/1.webp", "Misato/2.webp", "Misato/3.webp", "Misato/4.webp", "Misato/5.webp", "Misato/6.webp", "Misato/7.webp",
         "Misato/8.webp", "Misato/9.webp", "Misato/10.webp", "Misato/11.webp", "Misato/12.webp"]
shinji = ["Shinji/1.webp", "Shinji/2.webp", "Shinji/3.webp", "Shinji/4.webp", "Shinji/5.webp", "Shinji/6.webp", "Shinji/7.webp",
         "Shinji/8.webp", "Shinji/9.webp", "Shinji/10.webp", "Shinji/11.webp"]
secret = ["secret_end/1.webp", "secret_end/2.webp", "secret_end/3.webp", "secret_end/4.webp"]

secret_list = list()
@bot.message_handler(commands=['start'])
def welcome(message):
    ##keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/Asuka")
    item2 = types.KeyboardButton("/Rey")
    item3 = types.KeyboardButton("/Misato")
    item4 = types.KeyboardButton("/Shinji")
    markup.add(item1, item2, item3, item4)
    if(len(secret_list) == 4):
        item5 = types.KeyboardButton("/Secret")
        markup.add(item1, item2, item3, item4, item5)
    sti = open("Asuka/1.webp", 'rb')
    bot.send_sticker(message.chat.id, sti, reply_markup=markup)
    bot.send_message(message.chat.id, "Добро пожаловать, <b>{0.first_name}</b>!\nЯ <b>{1.first_name}</b>! Здесь ты можешь общаться с персонажами аниме Евангелион\nВыбери своего любимого персонажа, после чего я буду отвечать на каждое твоё сообщение стикером с персонажем\nЧтобы сменить персонажа, введи команду /change или выбери имя на клавиатуре.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)




@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "/Asuka":
        if "Asuka" not in secret_list:
            secret_list.append('Asuka')
        config.eba = "Asuka"
    elif message.text == "/Rey":
        if "Rey" not in secret_list:
            secret_list.append('Rey')
        config.eba = "Rey"
    elif message.text == "/Misato":
        if "Misato" not in secret_list:
            secret_list.append('Misato')
        config.eba = "Misato"
    elif message.text == "/Shinji":
        if "Shinji" not in secret_list:
            secret_list.append('Shinji')
        config.eba = "Shinji"
    if len(secret_list) == 4:
        if message.text == "/IkariGendo":
            config.eba = "Secret"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/Asuka")
    item2 = types.KeyboardButton("/Rey")
    item3 = types.KeyboardButton("/Misato")
    item4 = types.KeyboardButton("/Shinji")
    markup.add(item1, item2, item3, item4)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if(len(secret_list) == 4):
        item5 = types.KeyboardButton("/IkariGendo")
        markup.add(item1, item2, item3, item4, item5)
    if(config.eba=="Asuka"):
        sti = open(random.choice(asuka), 'rb')
        bot.send_sticker(message.chat.id, sti, reply_markup=markup)
    if(config.eba=="Rey"):
        sti = open(random.choice(rey), 'rb')
        bot.send_sticker(message.chat.id, sti, reply_markup=markup)
    if(config.eba =="Shinji"):
        sti = open(random.choice(shinji), 'rb')
        bot.send_sticker(message.chat.id, sti, reply_markup=markup)
    if(config.eba =="Misato"):
        sti = open(random.choice(misato), 'rb')
        bot.send_sticker(message.chat.id, sti, reply_markup=markup)
    if(config.eba =="Secret"):
        sti = open(random.choice(secret), 'rb')
        bot.send_sticker(message.chat.id, sti, reply_markup=markup)




bot.polling(none_stop=True)

