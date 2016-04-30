class Matrix(object):
    def __init__(self, matrix):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix

    def __str__(self):
        row_str = ''
        for row in self.matrix:
            row_str += '['
            for cell in row:
                row_str += str(cell) + ' '
            row_str += ']\n'
        return row_str

    def zero_rows_and_cols(self):
        zero_rows = set()
        zero_cols = set()
        for row_num, row in enumerate(self.matrix):
            for col_num, cell in enumerate(row):
                if cell == 0:
                    zero_rows.add(row_num)
                    zero_cols.add(col_num)
        for row in zero_rows:
            self.set_row_to_zero(row)
        for col in zero_cols:
            self.set_col_to_zero(col)

    def set_row_to_zero(self, row_num):
        for col_num in range(self.n):
            self.matrix[row_num][col_num] = 0

    def set_col_to_zero(self, col_num):
        for row_num in range(self.m):
            self.matrix[row_num][col_num] = 0