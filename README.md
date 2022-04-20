# ::speech_balloon: Python - Telegram-bot 
![version PyPi](https://img.shields.io/pypi/v/python-telegram-bot?color=orange&label=pypi)
![vesrion Python](https://img.shields.io/pypi/pyversions/p)
![Followers in GitHub](https://img.shields.io/github/followers/3?style=social)

**Поисковик-bot** - this telegram bot was created to simpify the process of searching for any information through [telegram](https://telegram.org/). 

**The Idea** of creating the bot was taken from the Internet and developed by me for an individual project. 

## **Installations**
___
Install the current version with PyPI:

```
pip install python-telegram-bot 
```
Also intall wikipedia API:

```
pip install wikipedia
```
## **Usage**
___
+ I added 2 buttons to the bot using the function
```python
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
```
*Thees buttons will allow you to determine in whic language the bot will continue to function* 

+ Afret the user selects the language, the `search` function will start and, depending on the choise this function will work in `Russian` or in `English`

```python
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
```
+ In this exemplem, the user has selected `Russian`
## **Contributing**
___
Bug reports and/or pull requests are welcome
## **License**
___
*While this project does'nt have licesnse, as it 
is'nt available in the public sites*

