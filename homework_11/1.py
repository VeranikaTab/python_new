# Создайте класс Матрица. Добавьте методы для:
# - вывода на печать
# - сравнения
# - сложения
# * умножения матриц

class Matrix:
    """класс Матрица"""
    def __init__(self, matrix):
        """Проверим, что матрица задана правильно (все строки имеют одинаковую длину)"""
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")

        self.matrix = matrix

    def __str__(self):
        """Преобразование матрицы в строку для вывода"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        """Сравнение двух матриц"""
        return self.matrix == other.matrix

    def __add__(self, other):
        """Сложение двух матриц"""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для сложения размеры матриц должны совпадать")

        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        """Умножение двух матриц"""
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")

        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)


m1 = Matrix([[1, 2, 5], [3, 4, 8], [5, 5, 6]])
m2 = Matrix([[2, 1, 0], [0, 1, 5], [5, 4, 8]])

print(m1)
print()
print(m2)
print()

print(Matrix.__eq__.__doc__)
print(m1 == m2)
# print(Matrix.__eq__(m1, m2))
print()

print(Matrix.__add__.__doc__)
# print(Matrix.__add__(m1, m2))
print(m1 + m2)
print()

print(Matrix.__mul__.__doc__)
print(m1 * m2)
# print(Matrix.__mul__(m1, m2))
print()
