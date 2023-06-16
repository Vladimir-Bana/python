import telebot
from telebot import types


bot = telebot.TeleBot("5142597765:AAEA7SdgqQ8VV7H6x1gA5JzdnOIwYLb217s")

name=""
surname=""
age=0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.send_message(message.from_user.id, "Привет меня зовут Бот давай с тобой познакомимся")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
 # bot.reply_to(message, message.text)
    if message.text.lower()=="привет":
        bot.send_message(message.from_user.id, "Привет, рад знакомству")
    elif message.text=="/reg":
        bot.send_message(message.from_user.id, "Здраствуй, как вас зовут?")
        bot.register_next_step_handler(message, nameReg)

    else:
        bot.send_message(message.from_user.id, "я не понимаю тебя")


def nameReg(message):
    global name
    name=message.text
    bot.send_message(message.from_user.id, "Введите вашу фамилию")
    bot.register_next_step_handler(message, surnameReg)

def surnameReg(message):
    global surname
    surname=message.text
    bot.send_message(message.from_user.id, "Введите ваш возраст")
    bot.register_next_step_handler(message, ageReg)

def ageReg(message):
    global age
    while age==0:
        try:
            age=int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Введите возраст цифрами")
    keyword=types.InlineKeyboardMarkup()
    button_yes=types.InlineKeyboardButton(text="Да",callback_data="yes")
    button_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
    keyword.add(button_yes,button_no)
    #keyword.add(button_no)
    mess = f"Вас зовут {name} {surname} и ваш возраст {age},верно ли?"
    bot.send_message(message.from_user.id, text=mess, reply_markup=keyword )


@bot.callback_query_handler(func=lambda call: True)
def query_button(call):
    if call.data=="yes":
        bot.send_message(call.message.chat.id,"Я вас запомнил, через время внесу вас в базу!")
    elif call.data=="no":
        bot.send_message(call.message.chat.id, "Давай попробуем еще раз. Как тебя зовут?")
        bot.register_next_step_handler(call.message, nameReg)

bot.infinity_polling()