def move_left(stick, table):
    pass


def add_stick(stick, table):
    color_index = 0
    for y_index in range(stick.y_index, stick.y_index + 3):
        # print(table, stick.colors)
        table.table[y_index][stick.x_index] = stick.colors[color_index]
        color_index += 1


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
