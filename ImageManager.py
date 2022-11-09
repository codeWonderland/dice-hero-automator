import math
import pyautogui
from PIL import Image

def take_screenshot(window_coords):
    screenshot = pyautogui.screenshot()
    
    # Setting the points for cropped image
    left = window_coords['pos_x']
    top = window_coords['pos_y']
    right = window_coords['pos_x'] + window_coords['width']
    bottom = window_coords['pos_y'] + window_coords['height']
    
    # Cropped image of above dimension
    # (It will not change original image)
    phone_screen = screenshot.crop((left, top, right, bottom))
    
    return phone_screen


def image_scan(image, bevel_color, horizontal = True, inc = True):
    dim_a = image.height
    dim_b = image.width

    if not horizontal:
        dim_a = image.width
        dim_b = image.height

    scan_lines = [
        5,
        dim_a / 6,
        dim_a * 2/6,
        dim_a * 3/6,
        dim_a * 4/6,
        dim_a * 5/6,
        dim_a - 5
    ]

    earliest_boundary = dim_b

    if not inc:
        earliest_boundary = 0

    for y in scan_lines:
        img_range = range(0, dim_b - 1)

        if not inc:
            img_range = range(dim_b - 1, 0, -1)

        for x in img_range:
            px = get_pixel_by_coords(image, x, y) if horizontal else get_pixel_by_coords(image, y, x)

            if (
                px[0] > bevel_color[0] or
                px[1] > bevel_color[1] or
                px[2] > bevel_color[2]
            ) and (
                (x < earliest_boundary and inc) or
                (x > earliest_boundary and not inc)
            ):
                earliest_boundary = x
                break
    
    return earliest_boundary


def standardize_screenshot(phone_screen):
    boundary_color = (35, 35, 35)
    
    top = image_scan(phone_screen, boundary_color, horizontal = False)
    bottom = image_scan(phone_screen, boundary_color, horizontal = False, inc = False)
    left = image_scan(phone_screen, boundary_color)
    right = image_scan(phone_screen, boundary_color, inc = False)
    
    phone_screen = phone_screen.crop((left, top, right, bottom))

    return phone_screen


def get_pixel_by_coords(image, x, y):
    px = image.load()
    return px[x, y]


def get_pixel(image, x_perc, y_perc):
    x_pos = math.floor(image.width * x_perc)
    y_pos = math.floor(image.height * y_perc)

    px = image.load()

    return px[x_pos, y_pos]


def view_color(color):
    print(color)
    image = Image.new(mode="RGB", size=(200, 200), color=color)
    image.show()


def view_pixel(image, x_perc, y_perc):
    pixel_color = get_pixel(image, x_perc, y_perc)
    view_color(pixel_color)



def pos_from_screen_coords(window_coords, phone_screen, game_coords):
    game_x_pos = math.floor(phone_screen.width * game_coords['x'])
    game_y_pos = math.floor(phone_screen.height * game_coords['y'])
    x_pos = window_coords['pos_x'] + game_x_pos
    y_pos = window_coords['pos_y'] + game_y_pos

    return x_pos, y_pos

