from datetime import datetime

def write(answer):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{answer}. Время запроса: {datetime.now()} \n')
