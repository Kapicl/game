from tkinter import *
from pickle import load, dump

from main import finish_id


# область функций
def set_status(status_text, color='black'):
    canvas.itemconfig(text_id, text=status_text, fill=color)

def pause_toggle():
    global pause
    pause = not pause
    if pause:
        set_status('Время пить чай!')
    else:
        set_status('Вперёд!')

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


def check_finish():
    global game_over

    coords_player1 = canvas.coords(player1)
    coords_player2 = canvas.coords(player2)
    coords_finish = canvas.coords(finish_id)

    x1_right = coords_player1[2]
    x2_right = coords_player2[2]
    x_finish = coords_finish[0]

    if x1_right >= x_finish:
        set_status('Победил красный игрок!', player1_color)
        game_over = True

    if x2_right >= x_finish:
        set_status('Победил синий игрок!', player2_color)
        game_over = True

def menu_enter():
    if menu_current_index == 0:
        game_resume()
    elif menu_current_index == 1:
        game_new()
    elif menu_current_index == 2:
        game_save()
    elif menu_current_index == 3:
        game_load()
    elif menu_current_index == 4:
        game_exit()

def game_new():
    global game_over, pause
    game_over = False
    pause = False
    canvas.coords(player1, x1, y1, x1 + player_size, y1 + player_size)
    canvas.coords(player2, x2, y2, x2 + player_size, y2 + player_size)
    set_status('Вперёд!', 'black')

def game_resume():
    global menu_mode, pause
    if not game_over:
        menu_hide()
        pause = False
        set_status('Вперёд!', 'black')
    else:
        set_status('Игра уже завершена. Начните новую игру.', 'red')

def game_save():
    x1 = canvas.coords(player1)[0]
    x2 = canvas.coords(player2)[0]
    data = [x1, x2]
    with open('save.dat', 'wb') as f:
        dump(data, f)
        set_status('Сохранено')

def game_load():
    global x1, x2
    with open('save.dat', 'rb') as f:
        data = load(f)
        x1, x2 = data
        canvas.coords(player1, x1, y1, x1 + player_size, y1 + player_size)
        canvas.coords(player2, x2, y2, x2 + player_size, y2 + player_size)
        set_status('Вперёд!')

def game_exit():
    print('Выходим из игры')
    exit()


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

# область переменных
game_width = 800
game_height = 800
menu_mode = True
menu_options = ['Возврат в игру', 'Новая игра', 'Сохранить', 'Загрузить', 'Выход']
menu_current_index = 3
menu_options_id = []


KEY_UP = 87
KEY_DOWN = 83
KEY_ESC = 27
KEY_ENTER = 13

player_size = 100
x1, y1 = 50, 50
x2, y2 = x1, y1 + player_size + 100
player1_color = 'red'
player2_color = 'blue'

x_finish = game_width - 50

KEY_PLAYER1 = 39
KEY_PLAYER2 = 68
KEY_PAUSE = 19

SPEED = 12

game_over = False
pause = False

game_width = 800
game_height = 800

# Окно и объекты
window = Tk()
window.title('DMEC')

canvas = Canvas(window, width=game_width, height=game_height, bg='white')
canvas.pack()
menu_create(canvas)
player1 = canvas.create_rectangle(x1,
                                  y1,
                                  x1 + player_size,
                                  y1 + player_size,
                                  fill=player1_color)
player2 = canvas.create_rectangle(x2,
                                  y2,
                                  x2 + player_size,
                                  y2 + player_size,
                                  fill=player2_color)
finish_id = canvas.create_rectangle(x_finish,
                                    0,
                                    x_finish + 10,
                                    game_height,
                                    fill='black')

text_id = canvas.create_text(x1,
                             game_height - 50,
                             anchor=SW,
                             font=('Arial', '25'),
                             text='Вперед!')


# Функции обратного вызова
window.bind('<KeyRelease>', key_handler)
window.mainloop()