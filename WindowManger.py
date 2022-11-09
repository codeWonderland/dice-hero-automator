import sh

def find_class(xprop_array_item):
    if "WM_CLASS(STRING)" in xprop_array_item:
        return True
    else:
        return False


def get_window_coords(window_id):
    window_info = sh.xwininfo("-id", window_id)

    data = {
        'pos_x': 'Absolute upper-left X',
        'pos_y': 'Absolute upper-left Y',
        'width': 'Width',
        'height': 'Height'
    }

    result = {}

    for line in window_info.splitlines():
        if not ':' in line:
            continue

        field_name, field_value = line.strip().split(':', 1)
        
        for key, value in data.items():
            if value == field_name:
                result[key] = int(field_value)

    return result
