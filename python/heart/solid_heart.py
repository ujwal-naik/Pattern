# Adjust the size by changing the range steps
for row in range(15, -15, -1):
    for col in range(-30, 30):
        # Heart shape equation
        x = col * 0.04
        y = row * 0.1
        if ((x**2 + y**2 - 1)**3 - x**2 * y**3) <= 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
