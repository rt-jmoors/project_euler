def compute_adjacents(matrix):
    """
    Compute  all combinations of products in the matrix in directions up,down, left, right or diagonally

    :param matrix: a 4 x 4 numpy array
    :return:
    """
    products = []
    grid_size = len(matrix)

    product_row = 1
    product_col = 1
    product_left = 1
    product_right = 1
    # calculate row, column and diagonal products
    for i in range(0, grid_size):
        for elem in matrix[i]:
            product_row *= elem
        for elem in matrix[:, i]:
            product_col *= elem

        products.append(product_row)
        products.append(product_col)
        product_row = 1
        product_col = 1

        product_left *= matrix[i, i]
        product_right *= matrix[grid_size - 1 - i, i]

    products.append(product_left)
    products.append(product_right)

    return products
