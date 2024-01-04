def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element in each row is always 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle

# Example usage:
# Uncomment the following lines if you want to test the function using the
# provided main script.

# def print_triangle(triangle):
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))
#
# if __name__ == "__main__":
#     print_triangle(pascal_triangle(5))
