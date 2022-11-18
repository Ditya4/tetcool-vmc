import pygame
from time import time
import model
import view
import control




rows = 15
columns = 11
size = 40
delta_t = 1
time_delay = 30
button_press_delta = 0.2
done = False
stick_count = 0
start = time()

table = model.Table(rows, columns)
render = view.Render(table.rows, table.columns, size)
# table.table[2][5] = 5
# render(table.table)
# pygame.time.delay(time_delay)
left_button_pressed = 0
right_button_pressed = 0
up_button_pressed = 0
down_button_pressed = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    '''
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            left_button_pressed = 0

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            right_button_pressed = 0
    '''
    if stick_count == 0:
        stick = model.Stick()
        if not control.add_stick(stick, table):
            print("Game Over.")
            done = True
        stick_count = 1

    if time() - start > delta_t:
        stick_count = control.move_down(stick, table)
        start = time()
        # continue

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if not left_button_pressed:
            control.move_left(stick, table)
            left_button_pressed = 1
            left_button_pressed_time_start = time()
        if left_button_pressed:
            left_button_pressed_time = (
                time() - left_button_pressed_time_start)
            if left_button_pressed_time > button_press_delta:
                control.move_left(stick, table)
                left_button_pressed_time_start = time()
    else:
        left_button_pressed = 0


    if keys[pygame.K_RIGHT]:
        # control.move_right(stick, table)
        if not right_button_pressed:
            control.move_right(stick, table)
            right_button_pressed = 1
            right_button_pressed_time_start = time()
        if right_button_pressed:
            right_button_pressed_time = (
                time() - right_button_pressed_time_start)
            if right_button_pressed_time > button_press_delta:
                control.move_right(stick, table)
                right_button_pressed_time_start = time()
    else:
        right_button_pressed = 0


    if keys[pygame.K_UP]:
        if not up_button_pressed:
            control.swich_colors(stick, table)
            up_button_pressed = 1
            up_button_pressed_time_start = time()
        if up_button_pressed:
            up_button_pressed_time = (
                time() - up_button_pressed_time_start)
            if up_button_pressed_time > button_press_delta:
                control.swich_colors(stick, table)
                up_button_pressed_time_start = time()
    else:
        up_button_pressed = 0

        # colors_sequence = swich_colors(colors_sequence)
        # win.fill((0, 0, 0))
        # stick = Stick(win, size, colors_sequence, x, y)
        # pygame.display.update()
        # pygame.time.delay(90)

    if keys[pygame.K_SPACE] or keys[pygame.K_DOWN]:
        if not down_button_pressed:
            control.put_down(stick, table)
            down_button_pressed = 1
            down_button_pressed_time_start = time()
        if down_button_pressed:
            down_button_pressed_time = (
                time() - down_button_pressed_time_start)
            if down_button_pressed_time > button_press_delta:
                control.put_down(stick, table)
                down_button_pressed_time_start = time()
    else:
        down_button_pressed = 0

        # y = window_height - size * 3
        # stick_count = 0
        # win.fill((0, 0, 0))
        # stick = Stick(win, size, colors_sequence, x, y)
        # pygame.display.update()
        # pygame.time.delay(30)


    render(table.table)
    pygame.time.delay(time_delay)




print(table)
