for row in range(12, -12, -1):
    for col in range(-15, 15):
        # Scale factors tailored for standard terminal character proportions
        x = col * 0.1
        y = row * 0.15
        
        # Check if the current coordinate is inside the heart
        is_inside = (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0
        
        # Check neighbors to identify if it is on the boundary
        is_boundary = False
        if is_inside:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = (col + dc) * 0.1
                ny = (row + dr) * 0.15
                if (nx**2 + ny**2 - 1)**3 - nx**2 * ny**3 > 0:
                    is_boundary = True
                    break
                    
        if is_boundary:
            print("*", end="")
        else:
            print(" ", end="")
    print()
