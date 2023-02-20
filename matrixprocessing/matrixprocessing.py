def matrix_enter(rows, columns):
    matrix = []
    for i in range(0, rows):
        row = input().split()[:columns]
        matrix.append([])
        for j in range(0, columns):
            matrix[i].append(float(row[j]))
    return matrix


def matrix_print(matrix):
    if matrix is None:
        return None
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=' ')
        print("")


def matrix_round(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(matrix[i][j]) if matrix[i][j] == round(matrix[i][j]) else matrix[i][j]
    return matrix


def matrix_add(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print('Sizes of matrix are not equal')
        return None
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1[0])):
            matrix1[i][j] += matrix2[i][j]
    return matrix_round(matrix1)


def matrix_multiply_constant(matrix, const):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            matrix[i][j] *= const
    return matrix_round(matrix)


def matrix_multiply_matrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print('Numbers of columns of first matrix and number of rows of second matrix are not equal')
        return None
    matrix = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix2[i])):
            result = 0
            for k in range(0, len(matrix2)):
                result += matrix1[i][k] * matrix2[k][j]
            matrix[i][j] = int(result) if round(result) == 0 else result
    return matrix_round(matrix)


def matrix_transpose(matrix, transpose_type):
    if transpose_type not in [1, 2, 3, 4]:
        print('The type hasn`t exist')
        return None
    matrix_transpose = []
    if transpose_type == 1:
        matrix_transpose = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[i])):
                matrix_transpose[i][j] = matrix[j][i]
    elif transpose_type == 2:
        matrix_transpose = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[i])):
                matrix_transpose[i][j] = matrix[len(matrix) - 1 - j][len(matrix[i]) - 1 - i]
    elif transpose_type == 3:
        matrix_transpose = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[i])):
                matrix_transpose[i][j] = matrix[i][len(matrix[0]) - 1 - j]
    elif transpose_type == 4:
        matrix_transpose = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[i])):
                matrix_transpose[i][j] = matrix[len(matrix) - 1 - i][j]
    return matrix_round(matrix_transpose)


def matrix_determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print('Determinant for non-square matrix doesn`t exist')
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for i in range(0, len(matrix)):
        minor = [[0 for j in range(len(matrix) - 1)] for i in range(len(matrix[0]) - 1)]
        for j in range(1, len(matrix)):
            shift = 0
            for k in range(0, len(matrix)):
                if k == i:
                    shift = 1
                    continue
                minor[j - 1][k - shift] = matrix[j][k]
        det += ((-1) ** i) * matrix_determinant(minor) * matrix[0][i]
    return int(det) if det == round(det) else det


def matrix_reverse(matrix):
    if len(matrix) != len(matrix[0]):
        print('Reverse matrix for non-square matrix doesn`t exist')
        return None
    det = matrix_determinant(matrix)
    if det == 0:
        print('Reverse matrix for matrix with zero determinant doesn`t exist')
        return None
    transpose_matrix = matrix_transpose(matrix, 1)
    reverse_matrix = [[0 for j in range(len(transpose_matrix))] for i in range(len(transpose_matrix[0]))]
    for i in range(len(transpose_matrix)):
        for j in range(len(transpose_matrix[0])):
            minor = [[0 for j in range(len(transpose_matrix) - 1)] for i in range(len(transpose_matrix[0]) - 1)]
            row_shift = 0
            for k in range(len(transpose_matrix)):
                if k == i:
                    row_shift = 1
                    continue
                column_shift = 0
                for p in range(len(transpose_matrix[0])):
                    if p == j:
                        column_shift = 1
                        continue
                    minor[(k - row_shift)][(p - column_shift)] = transpose_matrix[k][p]
            reverse_matrix[i][j] = ((-1) ** (i + j)) * matrix_determinant(minor)
    return matrix_round(matrix_multiply_constant(reverse_matrix, 1/det))


def main_menu():
    while True:
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice:""", end="")
        choice = int(input())
        if choice == 0:
            return None
        elif choice == 2:
            print("Enter size of matrix:", end="")
            size = input().split(" ")
            print("Enter matrix:")
            matrix = matrix_enter(int(size[0]), int(size[1]))
            print("Enter constant:", end="")
            constant = float(input())
            matrix = matrix_multiply_constant(matrix, constant)
            matrix_print(matrix)
        elif choice == 4:
            print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice:''', end="")
            choice = int(input())
            print("Enter size of matrix:", end="")
            size = input().split(" ")
            print("Enter matrix:")
            matrix = matrix_enter(int(size[0]), int(size[1]))
            matrix = matrix_transpose(matrix, choice)
            matrix_print(matrix)
        elif choice == 5 or choice == 6:
            print("Enter size of matrix:", end="")
            size = input().split(" ")
            print("Enter matrix:")
            matrix = matrix_enter(int(size[0]), int(size[1]))
            if choice == 5:
                det = matrix_determinant(matrix)
                if det is None:
                    continue
                print('The result is:\n', det)
            elif choice == 6:
                matrix = matrix_reverse(matrix)
                matrix_print(matrix)
        elif choice == 1 or choice == 3:
            matrix = []
            print("Enter size of first matrix:", end="")
            size = input().split(" ")
            print("Enter first matrix:")
            first_matrix = matrix_enter(int(size[0]), int(size[1]))
            print("Enter size of second matrix:", end="")
            size = input().split(" ")
            print("Enter second matrix:")
            second_matrix = matrix_enter(int(size[0]), int(size[1]))
            if choice == 1:
                matrix = matrix_add(first_matrix, second_matrix)
            elif choice == 3:
                matrix = matrix_multiply_matrix(first_matrix, second_matrix)
            matrix_print(matrix)


main_menu()


