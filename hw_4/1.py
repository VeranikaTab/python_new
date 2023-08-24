# ✔ Напишите функцию для транспонирования матрицы
# ------------- с использованием функций

def print_matrix(matrix):

    for el in matrix:
        print(el)


def transp_matrix_(matrix_A_):
    temp = []
    for i in range(len(matrix_A_[0])):
        temp_col = []
        for j in range(len(matrix_A_)):
            temp_col.append(matrix_A_[j][i])
        temp.append(temp_col)
    return temp


matrix_A_ = [[7, 2, 0],
             [1, 3, 8],
             [8, 7, 6],
             [5, 4, 5]]

print_matrix(transp_matrix_(matrix_A_))

# -------------

matrix_A = [[7, 2, 0],
            [1, 3, 8],
            [8, 7, 6],
            [5, 4, 5]]

# Определим пустую матрицу обратного порядка
transp_matrix = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
        transp_matrix[j][i] = matrix_A[i][j]
# сохраняем результат транспонирования в пустой матрице

print("Транспонирование матрицы matrix_A: ")
for item in transp_matrix:
    print(item)
print()
