# Hollow Diamond Printer in Python

A lightweight, customizable Python script to generate and print hollow diamond shapes of any size in the terminal using standard loops.

## ✨ Features

- **Dynamic Sizing**: Adjust the diamond scale easily by passing a single integer parameter.
- **Hollow Center**: Automatically calculates boundaries to print only the outer shell.
- **Zero External Dependencies**: Built entirely using native Python loops.

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Quick Start

1. **Clone or copy** the script into a file named `diamond.py`:

```python
def print_hollow_diamond(n):
    """Prints a hollow diamond shape of size n."""
    # Upper half of the diamond
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(2 * i + 1):
            print("*" if j == 0 or j == 2 * i else " ", end="")
        print()

    # Lower half of the diamond
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1), end="")
        for j in range(2 * i + 1):
            print("*" if j == 0 or j == 2 * i else " ", end="")
        print()

if __name__ == "__main__":
    # Change this number to resize the diamond
    print_hollow_diamond(5)
```

2. **Run the script** from your terminal:

```bash
python diamond.py
```

### 📋 Sample Output (`n = 5`)

```text
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
```

## 🛠️ How It Works

- **Leading Spaces**: The expression `" " * (n - i - 1)` shifts the stars to the right to create the diamond's slope.
- **Boundary Validation**: The condition `j == 0 or j == 2 * i` identifies the exact outer edges of the pattern.
- **Hollow Core**: Any index that does not match the boundary condition defaults to a space `" "`.

