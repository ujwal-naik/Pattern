# Python Square Star Pattern Generator

A simple Python utility to print solid and hollow square star pattern shapes of customizable sizes using nested loops.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)


## Features
- **Solid Square:** Fills every grid position with a star (`*`).
- **Hollow Square:** Prints stars (`*`) only on the outer boundaries (edges), leaving the internal area empty.
- **Customizable Size:** Adjust the `n` variable to change the square dimensions dynamically.

## Installation
Clone or download the repository to your local machine:
```bash
git clone https://github.com
cd square-pattern-generator
```
Ensure you have **Python 3.x** installed. Check your version with:
```bash
python --version
```

## Usage
Run the script directly from your terminal:
```bash
python square_patterns.py
```

### Output Example (Size = 5)

**Solid Square:**
```text
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
```

**Hollow Square:**
```text
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
```

## Code Structure

The source file `square_patterns.py` contains the logic broken down as follows:

### 1. Solid Square Implementation
```python
def print_solid_square(n):
    for i in range(n):
        print("* " * n)
```

### 2. Hollow Square Implementation
```python
def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
```

# Concentric Square Pattern Generator

A lightweight Python script that generates a grid of concentric numerical squares. Given an integer `n`, the script calculates a \((2n - 1) \times (2n - 1)\) matrix where the numbers decrease step-by-step from `n` on the outermost layer down to `1` at the exact center.

## 🚀 Visual Example (`n = 4`)

The script dynamically calculates boundaries to create perfectly symmetric layers:

```text
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
```

## 🧠 How the Algorithm Works

Instead of using complex conditional state loops or modifying an existing 2D array, this algorithm uses a **mathematical distance-to-border approach** executed in \(O(N^2)\) time:

1. **Grid Setup**: Calculates the total grid diameter using `size = 2 * n - 1`.
2. **Coordinate Evaluation**: Iterates through every coordinate `(i, j)` in the grid.
3. **Boundary Distances**: Finds the absolute distance from the current cell to all four edges:
   - `top = i`
   - `left = j`
   - `bottom = size - 1 - i`
   - `right = size - 1 - j`
4. **Layer Value**: The closest edge (`min()`) determines which concentric ring the cell occupies. Subtracting this index from `n` yields the correct value: 
   \[\text{value} = n - \min(\text{top}, \text{left}, \text{bottom}, \text{right})\]

## 💻 Usage

### Prerequisites
* Python 3.x

### Running the Script

1. Copy the code into a file named `pattern.py`:

```python
def print_concentric_square(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j

            val = n - min(top, left, bottom, right)
            print(val, end=" ")
        print()

if __name__ == "__main__":
    # Change this value to scale the square
    print_concentric_square(n=4)
```

2. Run the script from your terminal:
```bash
python pattern.py
```

## ⚙️ Complexity Analysis

* **Time Complexity**: \(\mathcal{O}(N^2)\) where \(N\) is the input value `n`. The nested loops run exactly \((2n-1) \times (2n-1)\) times.
* **Space Complexity**: \(\mathcal{O}(1)\) Auxiliary Space. The algorithm prints the pattern directly to the standard output stream without storing the grid structure in memory.
