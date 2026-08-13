import math

def print_solid_circle(radius):
    # Scale factor adjusts for terminal character aspect ratio (height > width)
    aspect_ratio = 2.5 
    
    # Iterate through the grid from negative radius to positive radius
    for y in range(-radius, radius + 1):
        for x in range(int(-radius * aspect_ratio), int(radius * aspect_ratio) + 1):
            
            # Normalize the x coordinate back to the circle's math scale
            x_normalized = x / aspect_ratio
            
            # Calculate distance from the center (0,0)
            distance = math.sqrt(x_normalized**2 + y**2)
            
            # Print '*' if the point is inside or on the boundary
            if distance <= radius:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next row

if __name__ == "__main__":
    # Change the number below to make the circle larger or smaller
    print_solid_circle(radius=8)