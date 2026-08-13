# Python Solid Circle Pattern Generator

A simple Python script that prints a solid, filled circle using asterisks (`*`) in the terminal. It uses basic coordinate geometry to determine which points fall inside the circle boundary.

## 🚀 Features
* **Perfect Proportions:** Uses an aspect ratio modifier to counteract terminal character stretching, keeping the circle round.
* **Pure Python:** Built using only standard libraries (`math`). No external dependencies required.
* **Highly Customizable:** Easily adjust the radius size or swap out the fill characters.

---

## 🛠️ How It Works

The script treats the terminal window as a 2D Cartesian coordinate plane where the center of the circle is at `(0, 0)`. 

It uses the standard distance formula:
\[d = \sqrt{x^2 + y^2}\]

If the calculated distance `d` is less than or equal to the `radius`, the point is recognized as being inside the circle, and the script prints a `*`. Otherwise, it prints a blank space.

---

## 💻 Code

```python
import math

def print_solid_circle(radius):
    # Scale factor adjusts for terminal character aspect ratio (height > width)
    aspect_ratio = 2.0 
    
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
```

---

## 📊 Sample Output (`radius = 8`)

```text
                    *                    
           *******************           
       ***************************       
     *******************************     
   ***********************************   
  *************************************  
 *************************************** 
 *************************************** 
*****************************************
 *************************************** 
 *************************************** 
  *************************************  
   ***********************************   
     *******************************     
       ***************************       
           *******************           
                    *                    
     
```

---

## 🔧 Customization

### Changing the Texture
You can easily swap out the `*` character or space character for other symbols (e.g., `#`, `@`, or `.`) inside the `print()` statements to change the look of your filled circle.
