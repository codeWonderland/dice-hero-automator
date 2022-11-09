import sh
import time
from priorities import priority_list
from MouseManager import click_screen, move_mouse
from WindowManger import get_window_coords
from ImageManager import get_pixel, pos_from_screen_coords, standardize_screenshot, take_screenshot, view_pixel


def get_state(phone_screen):
    current_state = None
    
    for priority in priority_list:
        priority_active = True

        for indicator in priority['relevancy_indicators']:
            pixel_color = get_pixel(phone_screen, indicator['coords']['x'], indicator['coords']['y'])

            if (
                indicator['valid_colors']['r'](pixel_color[0]) and
                indicator['valid_colors']['g'](pixel_color[1]) and
                indicator['valid_colors']['b'](pixel_color[2])
            ):
                pass # we are doing exclusionary filtering, so we don't care about the result of this
            else:
                priority_active = False
        
        if priority_active:
            current_state = priority
            break

    return current_state


def test_mode_fn(phone_screen):
    while True:
        coords = input('please input coordinates to test')
        x = float(coords.split(',')[0])
        y = float(coords.split(',')[1])

        view_pixel(phone_screen, x, y)

        time.sleep(0.5)

        x_pos, y_pos = pos_from_screen_coords(window_coords, phone_screen, {'x': x, 'y': y})
        move_mouse(x_pos, y_pos)


def start_game(window_coords, test_mode = False, admin_mode = False):
    phone_screen = take_screenshot(window_coords)
    phone_screen = standardize_screenshot(phone_screen)

    if admin_mode:
        test_mode_fn(phone_screen)

    current_state = get_state(phone_screen)

    if current_state is not None:
        click_screen(window_coords, phone_screen, current_state)
    elif test_mode:
        test_mode_fn(phone_screen)
    else:
        click_screen(window_coords, phone_screen, priority_list[4])
        


while True:
    game_window = sh.xdotool("search", "--class", "scrcpy")
    
    window_coords = get_window_coords(game_window)

    start_game(window_coords)

    time.sleep(2)