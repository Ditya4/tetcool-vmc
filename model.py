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
        self.mark_set = set()

    def create_table(self):
        return np.zeros(self.rows * self.columns, np.int32).reshape(
                        self.rows, self.columns)

    def __str__(self):
        '''
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        '''
        result = ""
        for value in self.table:
            print(" " * 37, list(value), ",", sep="")
        return str(self.table)

    def mark_to_erase(self, list_to_mark):
        pass

    def look_for_three_or_more(self, y_index, x_index, y, x):
        print("found similar", self.table[y][x], "at", y_index, x_index,
              y, x)
        list_to_destroy = [(y_index, x_index)]
        print("list_to_destroy =", list_to_destroy)
        value = self.table[y][x]
        y_var = y
        y_step = y_index - y
        x_var = x
        x_step = x_index - x
        # print("before while step y =", y_step, "step x =", x_step)
        # print("before while y_var =", y_var, "x_var =", x_var)
        while (0 <= y_var < self.rows and 0 <= x_var < self.columns and
               self.table[y_var][x_var] == value):
            # print("in while step y =", y_step, "step x =", x_step)
            # print("in_while y_var =", y_var, "x_var =", x_var)
            # if 0 <= y_var < self.rows and 0 <= x_var < self.columns:
            if (y_var, x_var) not in list_to_destroy:
                list_to_destroy.append((y_var, x_var))
            y_var += y_step
            x_var += x_step
            print(list_to_destroy)
        else:
            y_var = y
            y_step = -y_step
            x_var = x
            x_step = -x_step
            while (0 <= y_var < self.rows and 0 <= x_var < self.columns and
                   self.table[y_var][x_var] == value):
                if 0 <= y_var < self.rows and 0 <= x_var < self.columns:
                    if (y_var, x_var) not in list_to_destroy:
                        list_to_destroy.append((y_var, x_var))
                    y_var += y_step
                    x_var += x_step

                print(list_to_destroy)
        if len(list_to_destroy) >= 3:
            for cell in list_to_destroy:
                self.mark_set.add(cell)




    def check_cell(self, y_index, x_index):
        '''
        We check all neighbors cells of cell which is getted as method
        parameters. If value in one is equal to getted we send those
        two cells into look_for_three_of_more method.
        '''
        value = self.table[y_index][x_index]
        print("checking cell", y_index, x_index, "with value",
              self.table[y_index][x_index])
        for y in range(y_index - 1, y_index + 2):
            for x in range(x_index - 1, x_index + 2):
                if 0 <= y < self.rows and 0 <= x < self.columns:
                    if y == y_index and x == x_index:
                        'pass middle cell'
                    else:
                        print("comparing with cell", y, x, "with value",
                              self.table[y][x])
                        if value == self.table[y][x]:
                            self.look_for_three_or_more(y_index, x_index, y, x)

    def erase_cell(self, y_index, x_index):
        print("###################we are erasing", y_index, x_index, "with value",
              self.table[y_index, x_index])
        while self.table[y_index][x_index] != 0:
            self.table[y_index][x_index] = self.table[y_index - 1][x_index]
            y_index -= 1
            # print(self.table)
            # print()

    def collapse_similar(self):
        '''
        we check all not zero cells
        '''
        self.mark_set = set()
        for y_index in range(2, self.rows):
            for x_index in range(self.columns):
                print("table", y_index, x_index, "=",
                      self.table[y_index][x_index])
                if self.table[y_index][x_index]:
                    self.check_cell(y_index, x_index)
                    # fill self.mark_set with cells to erase
        print("mark_set =", self.mark_set)
        mark_list = list(self.mark_set)
        mark_list.sort(key=lambda x: x[0], reverse=True)
        print("mark_list.sorted =", mark_list)
        while mark_list:
            cell_y, cell_x = mark_list.pop()
            print("need to erase", cell_y, cell_x)
            self.erase_cell(cell_y, cell_x)




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
