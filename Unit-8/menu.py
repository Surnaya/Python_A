import tkinter as tk
import export
from tkinter import ttk


def data_menu():
    wind = tk.Tk()
    wind.title('Меню базы данных продаж авто')
    wind.geometry('400x200+500+200')
    wind.minsize(400, 200)
    wind.maxsize(400, 200)
    wind.config(bg='#CCE5FF')

    tk.Button(wind, text='Создать общий отчет', command=wind_1).grid(row=0, column=0, stick='wens')
    tk.Button(wind, text='Список сотрудников', command=wind_2).grid(row=1, column=0, stick='wens')
    tk.Button(wind, text='Общая сумма продаж', command=wind_4).grid(row=2, column=0, stick='wens')
    tk.Button(wind, text='Сумма продаж по сотрудникам', command=wind_5).grid(row=3, column=0, stick='wens')
    wind.grid_columnconfigure(0, minsize=400)
    wind.grid_rowconfigure(0, minsize=50)
    wind.grid_rowconfigure(1, minsize=50)
    wind.grid_rowconfigure(2, minsize=50)
    wind.grid_rowconfigure(3, minsize=50)
    wind.mainloop()


def wind_1():
    wind1 = tk.Tk()
    wind1.title('Общий отчет')
    wind1.geometry('1500x600')
    wind1.config(bg='#CCE5FF')

    table = ttk.Treeview(wind1, show='headings')
    heads = ['Фамилия', 'Имя', 'Цвет', 'Модель', 'Производитель', 'Год', 'Цена']
    table['columns'] = heads
    for header in heads:
        table.heading(header, text=header, anchor='center')
        table.column(header, anchor='center')

    for row in export.all_data():
        table.insert('', tk.END, values=row)

    table.pack(expand=tk.YES, fill=tk.BOTH)

    wind1.mainloop()

label = ''

def wind_2():
    global label
    def get_name():
        #global label
        label['text'] = name_search.get()
        wind_3()
        # return search

    wind2 = tk.Tk()
    wind2.title('Список сотрудников')
    wind2.geometry('400x300+500+200')
    wind2.config(bg='#CCE5FF')

    table = ttk.Treeview(wind2, show='headings')
    heads = ['Фамилия', 'Имя']
    table['columns'] = heads
    for header in heads:
        table.heading(header, text=header, anchor='center')
        table.column(header, anchor='center')

    for row in export.all_employee():
        table.insert('', tk.END, values=row)

    table.pack(expand=tk.YES, fill=tk.BOTH)

    tk.Label(wind2, text='Введите фамилию для поиска').pack()
    name_search = tk.Entry(wind2)
    name_search.pack()
    ttk.Button(wind2, text='Найти', command=get_name).pack()

    label = tk.Label(wind2)
    #ttk.Button(wind2, text=f'Найти {label}', command=wind_3()).pack()


    wind2.mainloop()


def wind_3():
    wind3 = tk.Tk()
    wind3.title(f'Сотрудник ')  # фио выбранного сотрудника
    wind3.geometry('400x300+500+200')
    wind3.config(bg='#CCE5FF')

    table = ttk.Treeview(wind3, show='headings')
    heads = ['Цвет', 'Модель', 'Марка', 'Год', 'Прайс']
    table['columns'] = heads
    for header in heads:
        table.heading(header, text=header, anchor='center')
        table.column(header, anchor='center')

    for row in export.surname_search():
        table.insert('', tk.END, values=row)

    table.pack(expand=tk.YES, fill=tk.BOTH)

    wind3.mainloop()


def wind_4():
    wind4 = tk.Tk()
    wind4.title('Общая сумма продаж')
    wind4.geometry('400x150+500+200')
    wind4.config(bg='#CCE5FF')

    sum_label = tk.Label(wind4, text=f'Общая сумма продаж авто = {export.all_sum()}',
                         fg='black',
                         font=('Arial', 14, 'bold'),
                         padx=20,
                         pady=60
                         )
    sum_label.pack()

    wind4.mainloop()


def wind_5():
    wind5 = tk.Tk()
    wind5.title('Сумма продаж по сотрудникам')
    wind5.geometry('700x250+500+200')
    wind5.config(bg='#CCE5FF')

    table = ttk.Treeview(wind5, show='headings')
    heads = ['Фамилия', 'Имя', 'Общая сумма продаж']
    table['columns'] = heads
    for header in heads:
        table.heading(header, text=header, anchor='center')
        table.column(header, anchor='center')

    for row in export.empl_sum():
        table.insert('', tk.END, values=row)

    table.pack(expand=tk.YES, fill=tk.BOTH)

    wind5.mainloop()
