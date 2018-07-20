import math

def player_touch_circle(p_x, p_y, width, height, radius, c_x, c_y):
    x_area = range(p_x - radius, p_x + width + radius)
    y_area = range(p_y - radius, p_y + height + radius)
    if c_x in x_area and c_y in y_area:
        return True
    return False

def player_touch_obst(p_x, p_y, width, height, obst_list, obst_size, shuffle, return_list = False):
    ''' Код работает только когда размеры player больше cell_size (obst_size)'''
    rects_in_player_x = math.ceil(width / obst_size)
    rects_in_player_y = math.ceil(height / obst_size)

    int_rect_x = math.floor((p_x-shuffle) / obst_size)
    remainder_x = obst_size - width % obst_size

    int_rect_y = math.floor((p_y - shuffle) / obst_size)
    remainder_y = obst_size - height % obst_size

    left_remainder_x = p_x - (int_rect_x * obst_size+shuffle)
    left_remainder_y = p_y - (int_rect_y * obst_size + shuffle)

    if left_remainder_x > remainder_x:
        rects_in_player_x += 1
    if left_remainder_y > remainder_y:
        rects_in_player_y += 1


    l_rects = []
    for x in range(0, rects_in_player_x):
        for y in range(0, rects_in_player_y):
            l_rects.append([(int_rect_x + x) * obst_size + shuffle, (int_rect_y + y) * obst_size + shuffle])

    if return_list:
        return l_rects
    for rect in l_rects:
        if rect in obst_list:
            return True
    return False


