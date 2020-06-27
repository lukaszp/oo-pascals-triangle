import math

class PascalsTriangleMath:

    def value_in(self, coordinates, recurrence_function):
        row, column = coordinates
        if row == column: return 1
        if column == 0: return 1
        return recurrence_function((row -1, column -1), recurrence_function) + \
            recurrence_function((row -1, column), recurrence_function)
    
    def cast_mirrored_columns(self, coordinates):
        row, column = coordinates
        if column > (int(math.ceil((row +1) / 2.0)) -1): column = row -column
        return (row, column) 