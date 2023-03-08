def determinant(matrix):
    """
    Calculates the determinant of a square matrix.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            sign = (-1) ** j
            sub_matrix = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
            det += sign * matrix[0][j] * determinant(sub_matrix)
        return det
