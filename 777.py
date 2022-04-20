import wikipedia
import telebot
from telebot import types

wikipedia.set_lang('en')
bot = telebot.TeleBot('5246690792:AAElxHAbqH3yJK5nHWAd3YtaIFockodNpy8')

@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) 
        markup.row('English')
        markup.row('Russian')
        msg = bot.send_message(message.chat.id, 'Выберите язык', reply_markup=markup)
        bot.register_next_step_handler(msg, search)
def search(message):
    if message.text == 'Russian':
        sending_mess = f"<b>Привет {message.from_user.first_name}!</b>\n напишите что ищете и вы получите ваш ответ"
        bot.send_message(message.chat.id, sending_mess, parse_mode='html')
        @bot.message_handler(content_types=['text'])
        def mess(message):
            wikipedia.set_lang('ru')
            try:
                final_message = ''
                word=message.text.strip().lower()
                final_message = wikipedia.summary(word)
                msg = bot.send_message(message.chat.id, final_message, parse_mode='html')
            except wikipedia.exceptions.PageError:
                msg = bot.send_message(message.chat.id, 'инфа не найдена ')  
            bot.register_next_step_handler(msg, mess)
    elif message.text == 'English':
         sending_mes = f"<b>Hello {message.from_user.first_name}!</b>\n write what you are looking for and you will receive your answer"
         bot.send_message(message.chat.id, sending_mes, parse_mode='html')
         @bot.message_handler(content_types=['text'])
         def mes(message):
             try:
                 final_mesage = ''
                 wrd=message.text.strip().lower()
                 final_mesage = wikipedia.summary(wrd)
                 msg1 = bot.send_message(message.chat.id, final_mesage, parse_mode='html')
             except wikipedia.exceptions.PageError:
                 msg1 = bot.send_message(message.chat.id, 'informatoion not found')  
             bot.register_next_step_handler(msg1, mes)
bot.polling(none_stop=True)

# import wikipedia
# import telebot
# 
# bot = telebot.TeleBot('5246690792:AAElxHAbqH3yJK5nHWAd3YtaIFockodNpy8')
# 
# @bot.message_handler(commands=['start'])
# def start(message):
    # sending_mess = f"<b>Привет{message.from_user.first_name}!</b>\n что то то то то"
    # bot.send_message(message.chat.id, sending_mess, parse_mode='html')
# 
# @bot.message_handler(content_types=['text'])
# def mess(message):
    # try:
        # final_message = ''
        # word=message.text.strip().lower()
        # final_message = wikipedia.summary(word)
        # bot.send_message(message.chat.id, final_message, parse_mode='html')
    # except wikipedia.exceptions.PageError:
        # bot.send_message(message.chat.id, 'инфа не найдена ')
    # 
# bot.polling(none_stop=True)
# 
# 
# 
# 
# 
# 
# 
# 