import telebot

import sqlite3

from telebot import types

db = sqlite3.connect('bot_saves.db', check_same_thread=False)

c = db.cursor()

n = c.execute("SELECT * FROM articles").fetchall()
print(n)


bot = telebot.TeleBot('your Telegram bot Api')

k = -1
subject = ""
d =0
correct_day = ""
add1 = 0

n1 = ['Алгебра','Геометрия','Биология','Химия','Физика','Английский язык','История Украины','Всемирная история','Информатика','География','Украинский язык','Украинская литература','Зарубежная литература','Право','Основы Здоровья']
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    material = types.KeyboardButton('Материалы к урокам')
    add_record = types.KeyboardButton('Добавить запись')
    remove_record = types.KeyboardButton('Удалить запись')
    markup.add(material,add_record,remove_record)
    bot.send_message(message.chat.id, "Здравствуйте, этот бот создан для сохранения материалов к урокам",reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def photo(text):
    global n, add1
    if subject != "" and correct_day != "" and add1 == 0:
        ph = text.photo[-1].file_id

        # bot.send_photo(text.chat.id, ph)
        subject2 = (subject, correct_day, 'photo', ph)
        c.execute("INSERT INTO articles VALUES(?,?,?,?)", (subject2))
        db.commit()
        n = c.execute("SELECT * FROM articles").fetchall()
        add1 = 0

        bot.send_message(text.chat.id, "Запись успешно добавлена")



@bot.message_handler(content_types=['text'])
def text(message1):
    global k, subject, markup, d, correct_day, n, add1, start
    add1 = 0
    if message1.text == "Вернуться в начало":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        material = types.KeyboardButton('Материалы к урокам')
        add_record = types.KeyboardButton('Добавить запись')
        remove_record = types.KeyboardButton('Удалить запись')
        markup.add(material, add_record, remove_record)

        k = -1
        subject = ""
        d = 0
        correct_day = ""
        add1 = 0
        bot.send_message(message1.chat.id, "Скажите что вы хотите сделать ", reply_markup=markup)

    if message1.text == "Vhr5465263hfs":
        subject1 = (correct_day, subject)

        c.execute("""DELETE FROM articles WHERE day_month_year = (?) AND subject = (?)""", (subject1))
        db.commit()
        n = c.execute("SELECT * FROM articles").fetchall()
        add1 = 1

        bot.send_message(message1.chat.id, "Запись успешно удалена ")

    if len(message1.text) == 10 and message1.text[2] == '.' and message1.text[5] == '.' and k == 0:
        correct_day = message1.text
        add1 = 1
        for lesson in n:
            if lesson[0] == subject and lesson[1] == message1.text:

                d = 1
                if lesson[2] == "text":
                    bot.send_message(message1.chat.id, lesson[3])
                if lesson[2] == "photo":
                    bot.send_photo(message1.chat.id, lesson[3])

        if d == 0:
            bot.send_message(message1.chat.id, "Записей не найдено")
        correct_day = ""
        d = 0

    if len(message1.text) == 10 and message1.text[2] == '.' and message1.text[5] == '.' and k == 1:
        correct_day = message1.text
        add1 = 1
        bot.send_message(message1.chat.id, "Введите запись которую хотите добавить ")

    if len(message1.text) == 10 and message1.text[2] == '.' and message1.text[5] == '.' and k == 2:
        correct_day = message1.text
        add1 = 1
        bot.send_message(message1.chat.id, "Введите Код доступа для удаления записи")

    for lesson1 in n1:
        db.commit()
        if lesson1 == message1.text:
            add1 = 1

            subject = lesson1

            if k == 0:

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                start = types.KeyboardButton("Вернуться в начало")
                markup_list = []
                for a in n:
                    if a[0] == message1.text:
                        j = a[1]
                        markup_list.append(j)
                markup.add(start)
                if len(markup_list) > 0:

                    markup.add(*markup_list)

                    bot.send_message(message1.chat.id, "Выбирите число за которое хотите просмотреть запись",
                                     reply_markup=markup)

                else:
                    bot.send_message(message1.chat.id, "записей не найдено", reply_markup=markup)
                break

            if k == 1:
                markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

                start = types.KeyboardButton("Вернуться в начало")
                markup.add(start)

                bot.send_message(message1.chat.id,
                                 "Скажите число за которое хотите сохранить запись в формате dd.mm.yyyy",
                                 reply_markup=markup)
                break
            if k == 2:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                start = types.KeyboardButton("Вернуться в начало")
                markup_list = []
                for a in n:
                    if a[0] == message1.text:
                        j = a[1]
                        markup_list.append(j)

                if len(markup_list) > 0:
                    markup.add(start)
                    markup.add(*markup_list)

                    bot.send_message(message1.chat.id, "Выбирите число за которое хотите удалить запись",
                                     reply_markup=markup)

                else:
                    bot.send_message(message1.chat.id, "Записей не найдено")
                break

    if message1.text == "Материалы к урокам":
        add1 = 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start = types.KeyboardButton("Вернуться в начало")
        algebra = types.KeyboardButton('Алгебра')
        geometry = types.KeyboardButton('Геометрия')
        biology = types.KeyboardButton('Биология')
        chemistry = types.KeyboardButton('Химия')
        physics = types.KeyboardButton('Физика')
        english = types.KeyboardButton('Английский язык')
        ukraine_history = types.KeyboardButton('История Украины')
        world_history = types.KeyboardButton('Всемирная история')
        informatics = types.KeyboardButton('Информатика')
        geography = types.KeyboardButton('География')
        ukraine_language = types.KeyboardButton('Украинский язык')
        ukraine_literature = types.KeyboardButton('Украинская литература')
        world_literature = types.KeyboardButton('Зарубежная литература')
        pravo = types.KeyboardButton('Право')
        osn_zdor = types.KeyboardButton('Основы Здоровья')
        markup.add(start)
        markup.add(algebra, geometry, biology, chemistry, physics, english, ukraine_history, world_history, informatics,
                   geography, ukraine_language, ukraine_literature, world_literature, pravo, osn_zdor)
        bot.send_message(message1.chat.id, "Скажите какой урок вас интересует", reply_markup=markup)

        k = 0

    if message1.text == "Удалить запись":
        add1 = 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start = types.KeyboardButton('Вернуться в начало')
        algebra = types.KeyboardButton('Алгебра')
        geometry = types.KeyboardButton('Геометрия')
        biology = types.KeyboardButton('Биология')
        chemistry = types.KeyboardButton('Химия')
        physics = types.KeyboardButton('Физика')
        english = types.KeyboardButton('Английский язык')
        ukraine_history = types.KeyboardButton('История Украины')
        world_history = types.KeyboardButton('Всемирная история')
        informatics = types.KeyboardButton('Информатика')
        geography = types.KeyboardButton('География')
        ukraine_language = types.KeyboardButton('Украинский язык')
        ukraine_literature = types.KeyboardButton('Украинская литература')
        world_literature = types.KeyboardButton('Зарубежная литература')
        pravo = types.KeyboardButton('Право')
        osn_zdor = types.KeyboardButton('Основы Здоровья')
        markup.add(start)
        markup.add(algebra, geometry, biology, chemistry, physics, english, ukraine_history, world_history, informatics,
                   geography, ukraine_language, ukraine_literature, world_literature, pravo, osn_zdor)
        bot.send_message(message1.chat.id, "Скажите из какого урока вы хотите удалить запись", reply_markup=markup)

        k = 2

    if message1.text == "Добавить запись":
        add1 = 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        start = types.KeyboardButton("Вернуться в начало")

        algebra = types.KeyboardButton('Алгебра')
        geometry = types.KeyboardButton('Геометрия')
        biology = types.KeyboardButton('Биология')
        chemistry = types.KeyboardButton('Химия')
        physics = types.KeyboardButton('Физика')
        english = types.KeyboardButton('Английский язык')
        ukraine_history = types.KeyboardButton('История Украины')
        world_history = types.KeyboardButton('Всемирная история')
        informatics = types.KeyboardButton('Информатика')
        geography = types.KeyboardButton('География')
        ukraine_language = types.KeyboardButton('Украинский язык')
        ukraine_literature = types.KeyboardButton('Украинская литература')
        world_literature = types.KeyboardButton('Зарубежная литература')
        pravo = types.KeyboardButton('Право')
        osn_zdor = types.KeyboardButton('Основы Здоровья')
        markup.add(start)
        markup.add(algebra, geometry, biology, chemistry, physics, english, ukraine_history, world_history, informatics,
                   geography, ukraine_language, ukraine_literature, world_literature, pravo, osn_zdor)
        bot.send_message(message1.chat.id, "Скажите какой урок вас интересует для сохранения записи",
                         reply_markup=markup)
        k = 1

    elif k == 1 and len(correct_day) > 0 and len(subject) > 0 and add1 == 0:
        add1 = 0
        subject2 = (subject, correct_day, 'text', message1.text)

        c.execute("INSERT INTO articles VALUES(?,?,?,?)", (subject2))
        db.commit()
        n = c.execute("SELECT * FROM articles").fetchall()

        bot.send_message(message1.chat.id, "Запись успешно добавлена")
    add1 = 0

bot.polling(none_stop=True)



