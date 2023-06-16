# 5142597765:AAEA7SdgqQ8VV7H6x1gA5JzdnOIwYLb217s
import telebot

bot = telebot.TeleBot("5142597765:AAEA7SdgqQ8VV7H6x1gA5JzdnOIwYLb217s")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я бот Владимир 😄")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
  if message.text.lower() == "привет":
    bot.reply_to(message, "Привет!")
  elif message.text.lower() == "как дела?":
    bot.reply_to(message, "Отлично, а у тебя?")
  elif message.text.lower() == "как дела":
    bot.reply_to(message, "Отлично,а у тебя?")
  elif message.text.lower() == "хорошо":
    bot.reply_to(message, "Это круто!")
  elif message.text.lower() == "отлично":
    bot.reply_to(message, "Это круто!")
  elif message.text.lower() == "нормально":
    bot.reply_to(message, "Это хорошо!")
  elif message.text.lower() == "плохо":
      bot.reply_to(message, "Надеюсь, все будет хорошо!🥺")
  elif message.text.lower() == "что делаешь?":
    bot.reply_to(message, "С тобой говорю 😁")
  elif message.text.lower() == "что делаешь":
    bot.reply_to(message, "С тобой говорю 😁")
  elif message.text.lower() == "сколько тебе лет?":
    bot.reply_to(message, "Я был создан 02.02.22 😎.")
  elif message.text.lower() == "сколько тебе лет":
    bot.reply_to(message, "Я был создан 02.02.22 😎.")
  elif message.text.lower() == "пока":
    bot.reply_to(message, "Пока, удачи!")
bot.infinity_polling()