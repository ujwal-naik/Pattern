# Concentric Circles Pattern

A Python program that generates perfectly concentric circles using asterisks (*) in the terminal.

## Description

This program creates three concentric circular rings centered on a grid. It uses mathematical calculations to determine which positions should display an asterisk, taking into account terminal font aspect ratio for accurate circle proportions.

## Features

- **Grid-based rendering**: 65x31 character display
- **Multiple rings**: 3 concentric circles with radii of 5.0, 10.0, and 14.0 units
- **Aspect ratio compensation**: Automatically adjusts for terminal font dimensions (2.1 aspect ratio)
- **Dynamic tolerances**: Ensures thick, unbroken lines for each ring
- **Clean output**: No rendering gaps or latency issues

## How to Run

```bash
python "concentric circles.py"
```

## Output

The program displays three concentric circles made of asterisks (*) on a uniform grid:

```
                       *******************                       
                  *********           *********                  
               *****                         *****               
            *****                               *****            
          ****           ***************           ****          
        ****         ******           ******         ****        
       ***        ****                     ****        ***       
     ****       ***                           ***       ****     
    ****      ***                               ***      ****    
   ****      ***           ***********           ***      ****   
   ***      ***         *****       *****         ***      ***   
  ***      ***         ***             ***         ***      ***  
  ***      **         **                 **         **      ***  
  ***     ***        ***                 ***        ***     ***  
  ***     ***        **                   **        ***     ***  
  ***     ***        ***                 ***        ***     ***  
  ***      **         **                 **         **      ***  
  ***      ***         ***             ***         ***      ***  
   ***      ***         *****       *****         ***      ***   
   ****      ***           ***********           ***      ****   
    ****      ***                               ***      ****    
     ****       ***                           ***       ****     
       ***        ****                     ****        ***       
        ****         ******           ******         ****        
          ****           ***************           ****          
            *****                               *****            
               *****                         *****               
                  *********           *********                  
                       *******************                                       
```

## Customization

You can modify the following parameters in the code:

- **width** (default: 65): Grid width in characters
- **height** (default: 31): Grid height in characters
- **radii** (default: [5.0, 10.0, 14.0]): Radius of each circle ring
- **tolerances** (default: [0.60, 0.65, 0.70]): Drawing tolerance for line thickness
- **aspect_ratio** (default: 2.1): Terminal font aspect ratio (adjust to 2.2 for more vertical circles)

## Algorithm

1. Calculate the center point of the grid using float coordinates
2. For each position on the grid:
   - Calculate the Euclidean distance from the center
   - Compensate for terminal font aspect ratio
   - Check if the distance matches any ring radius (within tolerance)
   - Display an asterisk (*) if matched, space otherwise
3. Output the complete grid to the terminal

