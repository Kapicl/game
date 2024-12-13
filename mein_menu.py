from pickle import load, dump
from tkinter import *

# Глобальные переменные
menu_options = ['Возврат в игру', 'Новая игра', 'Сохранить', 'Загрузить', 'Выход']
menu_current_index = 0
menu_options_id = []
menu_mode = False


def menu_create(canvas):
    global menu_options_id
    offset = 0
    for menu_option in menu_options:
        option_id = canvas.create_text(400, 200 + offset, anchor=CENTER,
                                       font=('Arial', '25'),
                                       text=menu_option, fill='black',
                                       state='hidden')
        menu_options_id.append(option_id)
        offset += 50


def menu_show():
    global menu_mode
    menu_mode = True
    menu_update()


def menu_hide():
    global menu_mode
    menu_mode = False
    menu_update()


def menu_up():
    global menu_current_index
    if menu_current_index > 0:
        menu_current_index -= 1
    menu_update()


def menu_down():
    global menu_current_index
    if menu_current_index < len(menu_options) - 1:
        menu_current_index += 1
    menu_update()


def menu_update():
    global menu_options_id
    for element_id in menu_options_id:
        canvas.delete(element_id)
    menu_options_id.clear()
    if not menu_mode:
        set_status('Вперёд!', 'black')
        return

    offset = 0
    for menu_index, menu_option in enumerate(menu_options):
        font_style = ('Arial', '30', 'bold') if menu_index == menu_current_index else ('Arial', '25')
        option_id = canvas.create_text(400, 200 + offset, anchor=CENTER, font=font_style, text=menu_option,
                                       fill='black')
        menu_options_id.append(option_id)
        offset += 50

