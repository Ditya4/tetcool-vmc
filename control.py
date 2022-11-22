def put_down(stick, table):
    print("call control.put_down")
    for y_index in range(stick.y_index + 3, table.rows):
        print(y_index, table.table[y_index][stick.x_index])
        if table.table[y_index][stick.x_index]:
            erase_stick(stick, table)
            stick.y_index = y_index - 3
            draw_stick(stick, table)
            return
    else:
        erase_stick(stick, table)
        stick.y_index = table.rows - 3
        draw_stick(stick, table)


def swich_colors(stick, table):
    result_sequence = stick.colors[:]
    switched_color = result_sequence.pop(0)
    result_sequence.append(switched_color)
    stick.colors = result_sequence
    erase_stick(stick, table)
    draw_stick(stick, table)


def erase_stick(stick, table):
    print("call control.erase_stick")
    for y_index in range(stick.y_index, stick.y_index + 3):
        table.table[y_index][stick.x_index] = 0


def move_left(stick, table):
    '''
    if stick is not close to left side and there are no already
    color filled cells in the left of stick, then we erase stick,
    decrease x_index by 1 and draw stick at the new place
    '''
    if stick.x_index > 0:
        for y_index in range(stick.y_index, stick.y_index + 3):
            if table.table[y_index][stick.x_index - 1]:
                return
        erase_stick(stick, table)
        stick.x_index -= 1
        draw_stick(stick, table)


def move_right(stick, table):
    '''
    if stick is not close to right side and there are no already
    color filled cells in the right of stick, then we erase stick,
    increase x_index by 1 and draw stick at the new place
    '''
    if stick.x_index < table.columns - 1:
        for y_index in range(stick.y_index, stick.y_index + 3):
            if table.table[y_index][stick.x_index + 1]:
                return
        erase_stick(stick, table)
        stick.x_index += 1
        draw_stick(stick, table)


def add_stick(stick, table):
    print("call control.add_stick")
    color_index = 0
    for y_index in range(stick.y_index, stick.y_index + 3):
        if table.table[y_index][stick.x_index]:
            return 0
        print("------------- added color", stick.colors[color_index])
        table.table[y_index][stick.x_index] = stick.colors[color_index]
        color_index += 1
    return 1


def draw_stick(stick, table):
    print("call control.draw_stick")
    print(stick.y_index + 3, stick.x_index)
    if (stick.y_index + 3 < table.rows and
            table.table[stick.y_index + 2][stick.x_index] != 0) or (
            stick.y_index + 3 > table.rows):
        return 0
    color_index = 0
    for y_index in range(stick.y_index, stick.y_index + 3):
        table.table[y_index][stick.x_index] = stick.colors[color_index]
        color_index += 1
    return 1


def erase_old_y(stick_old_y, stick, table):
    print("call control.erase_old_y")
    table.table[stick_old_y][stick.x_index] = 0


def move_down(stick, table):
    print("call control.move_down")
    stick_old_y = stick.y_index
    stick.y_index += 1
    if not draw_stick(stick, table):
        return 0
    erase_old_y(stick_old_y, stick, table)
    print("in move down", table, stick.colors, "\n")
    return 1
