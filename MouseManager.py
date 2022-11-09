import sh
from ImageManager import pos_from_screen_coords

def click_mouse(x, y):
    move_mouse(x, y)
    command = "mouseclick 1"
    sh.xte(command)


def move_mouse(x_pos, y_pos):
    command = "mousemove {} {}".format(x_pos, y_pos)
    sh.xte(command)


def click_screen(window_coords, phone_screen, current_state):
    x_pos, y_pos = pos_from_screen_coords(window_coords, phone_screen, current_state['coords'])
    click_mouse(x_pos, y_pos)
