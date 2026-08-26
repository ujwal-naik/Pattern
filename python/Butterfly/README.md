# Butterfly Pattern Printers in Python

A collection of lightweight Python functions designed to print symmetric **Solid** and **Hollow** butterfly star structures using text formatting. This project serves as an educational resource for mastering string operations, control flow structures, and mathematical symmetry in terminal outputs.

---

## 🌟 Visual Preview

### 1. Solid Butterfly
```text
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
```

### 2. Hollow Butterfly
```text
*      *
**    **
* *  * *
*  **  *
*  **  *
* *  * *
**    **
*      *
```

---

## 🛠️ Code Implementations

Save the code below into a file named `butterfly.py`:

```python
def print_solid_butterfly(n):
    """Prints a complete filled butterfly star pattern."""
    print(f"\n--- Solid Butterfly (n={n}) ---")
    
    # Upper Half
    for i in range(1, n + 1):
        stars = '*' * i
        spaces = ' ' * (2 * (n - i))
        print(stars + spaces + stars)
        
    # Lower Half
    for i in range(n, 0, -1):
        stars = '*' * i
        spaces = ' ' * (2 * (n - i))
        print(stars + spaces + stars)


def print_hollow_butterfly(n):
    """Prints a boundary-only butterfly star pattern."""
    print(f"\n--- Hollow Butterfly (n={n}) ---")
    
    # Upper Half
    for i in range(1, n + 1):
        left_wing = '*' if i == 1 else '*' + ' ' * (i - 2) + '*'
        right_wing = '*' if i == 1 else '*' + ' ' * (i - 2) + '*'
        spaces = ' ' * (2 * (n - i))
        print(left_wing + spaces + right_wing)
        
    # Lower Half
    for i in range(n, 0, -1):
        left_wing = '*' if i == 1 else '*' + ' ' * (i - 2) + '*'
        right_wing = '*' if i == 1 else '*' + ' ' * (i - 2) + '*'
        spaces = ' ' * (2 * (n - i))
        print(left_wing + spaces + right_wing)


if __name__ == "__main__":
    # Change the value of size to scale the structures up or down
    size = 4
    print_solid_butterfly(size)
    print_hollow_butterfly(size)
```

---

## 📐 How the Algorithm Works

Each row of the grid is built dynamically inside loops using three primary components:
$$\text{Row Output} = \text{Left Wing} + \text{Middle Gap} + \text{Right Wing}$$

### 1. The Global Coordinate System
The program breaks execution down into an upper and lower structure:
* **Upper Structure:** Loops from row index `1` up to `n`.
* **Lower Structure:** Loops backward from row index `n` down to `1` using `range(n, 0, -1)`.

### 2. Math Formula Tracker
For any given row index $i$ inside a design scale of size $n$:

| Pattern Variant | Component | Equation / Rule | Behavior |
| :--- | :--- | :--- | :--- |
| **Both** | Middle Gap | `2 * (n - i)` | Spaces shrink as $i$ increases |
| **Solid** | Wings | `*` $\times$ $i$ | Stars fill up the column spaces linearly |
| **Hollow** | Wings (Base Case: $i = 1$) | `*` | Only one single point is placed |
| **Hollow** | Wings (General Case: $i > 1$) | `*` + (` ` $\times$ `(i - 2)`) + `*` | Spaces carve out the wing interior |

---

## 🚀 Execution Instructions

1. Ensure you have **Python 3.x** installed.
2. Run the script file using your terminal tool:
   ```bash
   python butterfly.py
   ```

## 📝 License
This project is open-source and free to use for educational purposes.
