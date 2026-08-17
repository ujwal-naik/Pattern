import math

def print_perfect_concentric_circles():
    # Grid parameters optimized for a standard terminal window
    width = 65
    height = 31
    
    # Calculate exact float center coordinates
    center_x = (width - 1) / 2.0
    center_y = (height - 1) / 2.0
    
    # Standard terminal font aspect ratio (adjust to 2.2 if circles look vertical)
    aspect_ratio = 2.1
    
    # Define the 3 distinct radii for the concentric rings
    radii = [5.0, 10.0, 14.0]
    
    # Dynamic tolerance to ensure thick, unbroken lines at larger distances
    tolerances = [0.60, 0.65, 0.70]

    for y in range(height):
        row_output = []
        for x in range(width):
            # Calculate normalized distance from the center point
            dx = (x - center_x) / aspect_ratio
            dy = y - center_y
            distance = math.sqrt(dx**2 + dy**2)
            
            # Check if this coordinate lands on any of the rings cleanly
            draw_star = False
            for r, tol in zip(radii, tolerances):
                if abs(distance - r) < tol:
                    draw_star = True
                    break  # Stop checking once we find a match for this spot
            
            if draw_star:
                row_output.append("*")
            else:
                row_output.append(" ")
                
        # Join characters to prevent printing latency gaps
        print("".join(row_output))

# Run the perfect concentric circle generator
print_perfect_concentric_circles()
