def put_down(stick, table):
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
    for y_index in range(stick.y_index, stick.y_index + 3):
        table.table[y_index][stick.x_index] = 0


def move_left(stick, table):
    if stick.x_index > 0:
        for y_index in range(stick.y_index, stick.y_index + 3):
            if table.table[y_index][stick.x_index - 1]:
                return
        erase_stick(stick, table)
        stick.x_index -= 1
        draw_stick(stick, table)


def move_right(stick, table):
    if stick.x_index < table.columns - 1:
        for y_index in range(stick.y_index, stick.y_index + 3):
            if table.table[y_index][stick.x_index + 1]:
                return
        erase_stick(stick, table)
        stick.x_index += 1
        draw_stick(stick, table)


def add_stick(stick, table):
    color_index = 0
    for y_index in range(stick.y_index, stick.y_index + 3):
        if table.table[y_index][stick.x_index]:
            return 0
        # print(table, stick.colors)
        table.table[y_index][stick.x_index] = stick.colors[color_index]
        color_index += 1
    return 1


def draw_stick(stick, table):
    print(stick.y_index + 3, stick.x_index)
    if (stick.y_index + 3 < table.rows and
            table.table[stick.y_index + 2][stick.x_index] != 0) or (
            stick.y_index + 3 > table.rows):
        return 0
    color_index = 0
    for y_index in range(stick.y_index, stick.y_index + 3):
        print(table, stick.colors)
        table.table[y_index][stick.x_index] = stick.colors[color_index]
        color_index += 1
    return 1


def erase_old_y(stick_old_y, stick, table):
    table.table[stick_old_y][stick.x_index] = 0


def move_down(stick, table):
    stick_old_y = stick.y_index
    stick.y_index += 1
    if not draw_stick(stick, table):
        return 0
    erase_old_y(stick_old_y, stick, table)
    return 1
