import numpy as np
from random import choice


class Table():
    '''
    also we create 2 invisible lines by adding +2 to rows at _init function,
    so we could create our stick
    at 0 level of table, and visually will be seas only last brick of it
    We create an array for our game field, filled with integer values,
    every value is a color which is equivalent to number.
    0 - black
    1 - red
    2 - blue
    3 - yellow
    4 - green
    5 - pink
    6 - 04FEFC(light blue)
    '''

    def __init__(self, rows, columns):
        self.rows = rows + 2
        self.columns = columns
        self.table = self.create_table()

    def create_table(self):
        return np.zeros(self.rows * self.columns, np.int32).reshape(
                        self.rows, self.columns)

    def __str__(self):
        return str(self.table)


class Stick():

    def __init__(self):
        colors_codes = range(1, 7)
        self.x_index = 5
        self.y_index = 0

        self.colors = []
        for unused in range(3):
            self.colors.append(choice(colors_codes))
        print(self.colors)



if __name__ == "__main__":
    rows = 15
    columns = 11

    table = Table(rows, columns)
    print(table)
