import telebot
import config
import logger as lg
import csv

bot = telebot.TeleBot(config.SOME_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome_handler(message):
    text = f'Привет, {message.from_user.first_name}. Это телефонный справочник\nЧтобы добавить новую запись /add\nПоиск по фамилии /search_lastname\nПоиск по имени /search_firstname'
    bot.reply_to(message, text)


@bot.message_handler(commands=['search_lastname'])
def get_message(message):
    text = 'Введите фамилию'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, lastname_search)

def lastname_search(msg):
    lastname = msg.text
    result = []
    with open("example.csv", encoding='utf-8') as tel_book:
        book_reader = csv.reader(tel_book, delimiter=",")
        for row in book_reader:
            if row[0] == lastname:
                result.append(row)

    if result == []:
        answer = 'Абонент не найден'
    else:
        answer = f'Найден абонент {result[0][0]} {result[0][1]} - номер телефона {result[0][2]}'


    lg.write(answer)
    bot.send_message(msg.chat.id, f'{answer}')

@bot.message_handler(commands=['search_firstname'])
def get_message(message):
    text = 'Введите имя'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, firstname_search)

def firstname_search(msg):
    firstname = msg.text
    result = []
    with open("example.csv", encoding='utf-8') as tel_book:
        book_reader = csv.reader(tel_book, delimiter=",")
        for row in book_reader:
            if row[1] == firstname:
                result.append(row)

    if result == []:
        answer = 'Абонент не найден'
    else:
        answer = f'Найден абонент {result[0][0]} {result[0][1]} - номер телефона {result[0][2]}'


    lg.write(answer)
    bot.send_message(msg.chat.id, f'{answer}')

@bot.message_handler(commands=['add'])
def get_message(message):
    text = 'Введите фамилию, имя, номер телефона через пробелы'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, add_data)

def add_data(msg):
    data_str = msg.text
    data_list = data_str.split()
    with open('example.csv', 'a', newline='') as tel_book:
        writer = csv.writer(tel_book, delimiter=",", lineterminator="\r\n")
        writer.writerows([data_list])
        answer = f'Спасибо, данные записаны\nДобавлен абонент {data_list[0]} {data_list[1]} номер телефона {data_list[2]}'       

    lg.write(answer)
    bot.send_message(msg.chat.id, f'{answer}')
if __name__ == '__main__':
    bot.polling(non_stop=True)
