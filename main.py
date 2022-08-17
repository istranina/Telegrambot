import random
import telebot
bot = telebot.TeleBot('5697704020:AAGOgx9WSa47_L8wBRGFrspb57h_va3a6cQ');

from telebot import types
first = ["Прислушиваться к интуиции сегодня стоит даже тем, кто привык игнорировать ее подсказки.","Вас ждет непростой, но все же довольно удачный день.","Первая половина дня будет особенно благоприятной, постарайтесь провести ее с пользой.","Проявите настойчивость, и вы добьетесь того, что прежде казалось почти невозможным.","Этот день будет благоприятным, хорошо подойдет для того, чтобы взяться за какой-то масштабный и сложный проект. "]
second = ["Но помните, что даже в этом случае не стоит забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с близкими родственниками.","рабочие вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру может ухудшиться самочувствие.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не предотвратить выгорание в конце месяца."]
third = ["Вторая половина дня будет благоприятной для общения, встреч в неформальной обстановке, разговоров с друзьями и романтических свиданий. Люди, которые прежде не нравились друг другу, могут неожиданно проникнуться взаимной симпатией..","Вторая половина дня хорошо подойдет для семейных дел. Ладить с родственниками будет легко, договориться об общих планах вы сможете быстро.","Вторая половина дня обещает важные новости.","Во второй половине дня может быть непросто сохранить хорошее настроение. Вы можете расстраиваться из-за пустяков, принимать близко к сердцу то, на что в другое время не обратили бы внимания.","Вторая половина дня будет насыщеннее и плодотворнее первой. Она хорошо подойдет для того, чтобы взяться за непростое дело или начать учиться тому, что кажется очень сложным, но столь же полезным."]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет! Ты готов? Сейчас я расскажу, что тебя ждёт сегодня.")
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши: Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "zodiac":

        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)

        bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)