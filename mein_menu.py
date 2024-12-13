from tkinter import Tk, Canvas, CENTER

# Глобальные переменные для меню
menu_options = ['Возврат в игру', 'Новая игра', 'Сохранить', 'Загрузить', 'Выход']
menu_options_id = []
menu_current_index = 0
menu_mode = False

def set_status(canvas, text, color='black'):
    canvas.itemconfig(text_id, text=text, fill=color)

def menu_create(canvas):
    offset = 0
    for menu_option in menu_options:
        option_id = canvas.create_text(400, 200 + offset, anchor=CENTER, font=('Arial', '25'), text=menu_option, fill='black')
        menu_options_id.append(option_id)
        offset += 50

def menu_show(canvas):
    global menu_mode
    menu_mode = True
    menu_update(canvas)

def menu_hide(canvas):
    global menu_mode
    menu_mode = False
    menu_update(canvas)

def menu_update(canvas):
    for menu_index in range(len(menu_options_id)):
        element_id = menu_options_id[menu_index]
        canvas.itemconfig(element_id, state='normal' if menu_mode else 'hidden')
        if menu_mode and menu_index == menu_current_index:
            canvas.itemconfig(element_id, fill='yellow')
        else:
            canvas.itemconfig(element_id, fill='black')

def menu_toggle():
    global menu_mode
    menu_mode = not menu_mode
