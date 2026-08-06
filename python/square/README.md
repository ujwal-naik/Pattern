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

