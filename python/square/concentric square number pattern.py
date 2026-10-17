def print_concentric_square(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            # Find the minimum distance to any of the 4 borders
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j
            
            val = n - min(top, left, bottom, right)
            print(val, end=" ")
        print()


# Example usage:
n = 4
print_concentric_square(n)
