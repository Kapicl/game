from tkinter import *
from pickle import load, dump
from main import *

def menu_toggle():
    global menu_mode
    if menu_mode:
        menu_hide()
    else:
        menu_show()

def key_handler(event):
    global menu_mode

    if event.keycode == KEY_ESC:
        menu_toggle()
        return

    if menu_mode:
        if event.keycode == KEY_UP:
            menu_up()
        elif event.keycode == KEY_DOWN:
            menu_down()
        elif event.keycode == KEY_ENTER:
            menu_enter()
        return

    if game_over:
        return

    if event.keycode == KEY_PAUSE:
        pause_toggle()
        return

    if pause:
        return

    if event.keycode == KEY_PLAYER1:
        canvas.move(player1, SPEED, 0)
    elif event.keycode == KEY_PLAYER2:
        canvas.move(player2, SPEED, 0)

    check_finish()

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
        if menu_index == menu_current_index:
            option_id = canvas.create_text(400, 200 + offset, anchor=CENTER, font=('Arial', '30', 'bold'),
                                           text=menu_option, fill='black')
        else:
            option_id = canvas.create_text(400, 200 + offset, anchor=CENTER, font=('Arial', '25'), text=menu_option,
                                           fill='black')
        menu_options_id.append(option_id)
        offset += 50

def menu_create(canvas):
    offset = 0
    for menu_option in menu_options:
        option_id = canvas.create_text(400, 200 + offset, anchor=CENTER, font=('Arial', '25'), text=menu_option,
                                       fill='black', state='hidden')
        menu_options_id.append(option_id)
        offset += 50

menu_create(canvas)
window.bind('<KeyRelease>', key_handler)
window.mainloop()
