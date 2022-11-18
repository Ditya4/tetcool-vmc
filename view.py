import pygame


class Render():
    '''
    Draw squares on canvas  for every not zero table object,
    all zeros fill with black color. from index row index = 2
    our array have +2 rows for creation a stick on 0 level and
    we need to display only rows from index 2.
    We have an array for our game field, filled with integer values,
    every value is a number which is equivalent to color.
    0 - black
    1 - red
    2 - blue
    3 - yellow
    4 - green
    5 - pygame.Color(252, 2, 252) pink
    6 - pygame.Color(4, 255, 252) light blue
    '''

    def __init__(self, rows, columns, size):
        self.rows = rows
        self.invisible_rows = 2
        self.columns = columns
        self.size = size
        self.canvas = self.create_canvas()
        pygame.init()
        self.colors_decode = {0: "black",
                              1: "red",
                              2: "blue",
                              3: "yellow",
                              4: "green",
                              5: pygame.Color(252, 2, 252),
                              6: pygame.Color(4, 255, 252),
                              }

    def create_canvas(self):
        window_height = self.size * (self.rows - self.invisible_rows)
        window_width = self.size * self.columns
        canvas = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Tetcool")
        return canvas

    def __call__(self, table):
        self.draw_table(table)

    def draw_table(self, table):
        self.canvas.fill((0, 0, 0))
        for i in range(self.rows):
            for j in range(self.columns):
                if table[i][j] and i >= self.invisible_rows:
                    '''
                    print((i - self.invisible_rows) * self.size,
                          j * self.size,
                          table[i][j],
                          self.colors_decode[
                              table[i][j]])
                    '''
                    pygame.draw.rect(
                        self.canvas,
                        self.colors_decode[table[i][j]],
                        (j * self.size, (i - self.invisible_rows) * self.size,
                         self.size, self.size))
                    pygame.draw.rect(
                        self.canvas,
                        self.colors_decode[0],
                        (j * self.size, (i - self.invisible_rows) * self.size,
                         self.size, self.size), 1)
        pygame.display.update()


if __name__ == "__main__":
    rows = 15
    columns = 11
    size = 40

    canvas = Render(rows, columns, size)
