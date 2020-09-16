import sys


def parse_and_validate_file(file, d):
    matrix = [[0 for x in range(d)] for y in range(d)]

    i = 0
    try:
        with open(file, 'r') as r_file:
            read_file = r_file.readlines()

            if len(read_file) != d:
                print('Matrix needs to be a regular one.')
                sys.exit(-1)

            for line in read_file:
                j = 0
                split_line = [num for num in line.split(',')]

                if '\n' in split_line:
                    split_line.remove('\n')

                split_line = [num.lstrip() for num in split_line]

                if len([num.isdigit() for num in split_line]) == d:
                    try:
                        if all([0 <= int(num) <= d for num in split_line]):
                            for el in split_line:
                                matrix[i][j] = int(el)
                                j += 1
                            i += 1

                        else:
                            print('Not all numbers are in the proper range.')
                            sys.exit(-1)

                    except ValueError:
                        print('An error occurred during casting string -> int.')

                else:
                    print('Not all elements are digits.')
                    sys.exit(-1)

            return matrix

    except IOError:
        print('An issue occurred during opening the file {}.'.format(file))


def print_matrix(matrix, d):
    for row in range(0, d):
        for col in range(0, d):
            print('{} '.format(matrix[row][col]), end='')
        print('')


def check_row_availability(matrix, row, number, d):
    if number in [matrix[row][i] for i in range(0, d)]:
        return True
    return False


def check_column_availability(matrix, col, number, d):
    if number in [matrix[i][col] for i in range(0, d)]:
        return True
    return False


def check_box_availability(matrix, row, col, number):
    for i in range(3):
        for j in range(3):
            if matrix[i + row][j + col] == number:
                return True
    return False


def find_free_position(matrix, d, pos_list):
    for i in range(d):
        for j in range(d):
            if matrix[i][j] == 0:
                pos_list[0] = i
                pos_list[1] = j

                return True
    return False


def number_availability(matrix, row, col, number, d):
    return not check_row_availability(matrix, row, number, d) \
           and not check_column_availability(matrix, col, number, d) \
           and not check_box_availability(matrix, row - row % 3, col - col % 3, number)


def solve_sudoku(matrix, d):
    pos_list = [0, 0]

    if not find_free_position(matrix, d, pos_list):
        return True

    row = pos_list[0]
    col = pos_list[1]

    for number in range(1, d + 1):
        if number_availability(matrix, row, col, number, d):
            matrix[row][col] = number

            if solve_sudoku(matrix, d):
                return True

            matrix[row][col] = 0

    return False


def flow(file):
    print('Enter the matrix dimension:')
    d = int(input())

    matrix = parse_and_validate_file(file, d)
    matrix_before = parse_and_validate_file(file, d)

    if solve_sudoku(matrix, d):
        print('------------------')
        print('Sudoku is solved!')
        print('------------------')
        print('Sudoku before:')
        print_matrix(matrix_before, d)
        print('')
        print('Sudoku after:')
        print_matrix(matrix, d)

    else:
        print('Sudoku can\t be solved!')


