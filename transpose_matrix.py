# Date:- 14 April 2024
# Program to Transpose a matrix using a nested loop


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row =[]
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)
    return transpose



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original Matrix:")
for row in matrix:
    print(row)

transposed_matrix = transpose_matrix(matrix)
print("Transpose Matrix:")
for row in transposed_matrix:
    print(row)