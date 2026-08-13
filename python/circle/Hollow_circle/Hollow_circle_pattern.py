import math

def print_circle_pattern(radius):
    # Scale factor adjusts for terminal character aspect ratio (height > width)
    aspect_ratio = 2.0 
    
    # Iterate through the grid from negative radius to positive radius
    for y in range(-radius, radius + 1):
        for x in range(int(-radius * aspect_ratio), int(radius * aspect_ratio) + 1):
            
            # Normalize the x coordinate back to the circle's math scale
            x_normalized = x / aspect_ratio
            
            # Calculate distance from the center (0,0)
            distance = math.sqrt(x_normalized**2 + y**2)
            
            # Print '*' if the point is on the boundary (with a small buffer)
            if radius - 0.5 < distance < radius + 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next row

# Run the function with a radius of 8
print_circle_pattern(8)
