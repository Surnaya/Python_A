from datetime import datetime

def write(some_str, result):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{some_str} = {result}. Время запроса: {datetime.now()} \n')
