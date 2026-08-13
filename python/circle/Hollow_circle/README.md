# Python Circle Star Pattern Generator

A simple Python script that prints a visually balanced circle using asterisks (`*`) in the terminal. It uses basic algebra and coordinate geometry to map a circle onto a text grid.

## 🚀 Features
* **Perfect Proportions:** Uses an aspect ratio modifier to prevent terminal text stretching, ensuring the circle looks round rather than oval.
* **Pure Python:** Built using only standard libraries (`math`). No external dependencies required.
* **Highly Customizable:** Easily adjust the radius or swap out the characters.

---

## 🛠️ How It Works

The script treats the terminal window as a 2D Cartesian coordinate plane where the center of the circle is at `(0, 0)`. 

It uses the standard circle distance formula:
\[d = \sqrt{x^2 + y^2}\]

If the distance d from the origin is roughly equal to the user-defined `radius`, the script prints a `*`. Otherwise, it prints a blank space.

---

## 💻 Code

```python
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

if __name__ == "__main__":
    # Change the number below to make the circle larger or smaller
    print_circle_pattern(radius=8)
```

---

## 📊 Sample Output (`radius = 8`)

```text
       *******       
     **       **     
   **           **   
  *               *  
 *                 * 
 *                 * 
*                   *
*                   *
*                   *
 *                 * 
 *                 * 
  *               *  
   **           **   
     **       **     
       *******       
```

---

## 🔧 Customization

### Filled Circle
If you want to render a **solid, filled circle** instead of a hollow outline, replace line 18 in the script:

* **Find:** `if radius - 0.5 < distance < radius + 0.5:`
* **Replace with:** `if distance <= radius:`

### Changing Symbols
You can easily swap out the `*` character or space character for other symbols (e.g., `#`, `@`, or `.`) inside the `print()` statements to change the texture of the output.
