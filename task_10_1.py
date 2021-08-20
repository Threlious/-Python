class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(self.matrix[i-1]):
                raise SyntaxError

    def __str__(self):
        matrix_join = [' '.join(map(str, self.matrix[i])) for i in range(len(self.matrix))]
        final_str = f''
        for i in range(len(matrix_join)):
            final_str += f'{matrix_join[i]}\n'
        return final_str

    def __add__(self, other):
        if len(other.matrix) != len(self.matrix) or len(other.matrix[0]) != len(self.matrix[0]):
            raise SyntaxError
        matrix_sum = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                      for i in range(len(self.matrix))]
        return Matrix(matrix_sum)


matrix_1 = Matrix([[3, 6, 7, 6], [0, -5, 9, 0], [9, 0, 0, 7]])
matrix_2 = Matrix([[3, 6, 0, 7], [0, -5, 8, 1], [8, -5, 0, 3]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
