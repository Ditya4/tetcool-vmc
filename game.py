import pygame
from time import time
import model
import view
import control




rows = 15
columns = 11
size = 40
delta_t = 1
time_delay = 3
done = False
stick_count = 0
start = time()

table = model.Table(rows, columns)
render = view.Render(table.rows, table.columns, size)
# table.table[2][5] = 5
# render(table.table)
# pygame.time.delay(time_delay)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if stick_count == 0:
        stick = model.Stick()
        control.add_stick(stick, table)
        stick_count = 1

    if time() - start > delta_t:
        stick_count = control.move_down(stick, table)
        start = time()
        # continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        control.move_left(stick, table)
        # if stick.x - size >= 0:
        #     x -= size

    if keys[pygame.K_RIGHT]:
        control.move_right(stick, table)
        # if stick.x + size < window_width:
        #     x += size

    if keys[pygame.K_UP]:
        control.swich_colors()
        # colors_sequence = swich_colors(colors_sequence)
        # win.fill((0, 0, 0))
        # stick = Stick(win, size, colors_sequence, x, y)
        # pygame.display.update()
        # pygame.time.delay(90)

    if keys[pygame.K_SPACE]:
        control.put_down()
        # y = window_height - size * 3
        # stick_count = 0
        # win.fill((0, 0, 0))
        # stick = Stick(win, size, colors_sequence, x, y)
        # pygame.display.update()
        # pygame.time.delay(30)


    render(table.table)
    pygame.time.delay(time_delay)




print(table)
