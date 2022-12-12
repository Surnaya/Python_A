import telebot
import config
import operation
import calc
import logger as lg

bot = telebot.TeleBot(config.SOME_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome_handler(message):
    text = 'Привет. Для вычислений операций с числами команда /calc'
    bot.reply_to(message, text)


@bot.message_handler(commands=['calc'])
def get_message(message):
    text = 'Введите пример для вычисления через пробелы'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, make_calc)


def make_calc(msg):
    some_str = msg.text
    some_tuple = operation.op(some_str)  # присвоить исходному кортежу переменную
    calc.init(some_tuple[0], some_tuple[1])  # инициализация переменных а и b
    if some_tuple[2] == '+':
        result = calc.sum()
    elif some_tuple[2] == '-':
        result = calc.dif()
    elif some_tuple[2] == '*' or some_tuple[2] == 'x':
        result = calc.mult()
    elif some_tuple[2] == '/':
        result = calc.div()
    else:
        result = 'операция не существует'

    lg.write(some_str, result)
    bot.send_message(msg.chat.id, f'{some_str} = {result}')

if __name__ == '__main__':
    bot.polling(non_stop=True)
