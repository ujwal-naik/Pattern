# Mathematical Heart Patterns in Python

This project contains elegant Python scripts that use algebraic geometry to render highly customizable **Solid** and **Hollow** heart shapes directly into your terminal.

---

## 🛠️ The Formula

Both patterns rely on the classic 3D heart algebraic equation:
\[(x^2 + y^2 - 1)^3 - x^2y^3 = 0\]

- **Solid Heart:** Prints characters for any coordinates where the equation evaluates to less than or equal to zero (≤ 0).
- **Hollow Heart:** Evaluates neighboring pixels. If a pixel is inside the heart but borders an outside pixel, it renders as a boundary character. This creates a clean, continuous 1-character thick outline.


##Exmaple
~~~
                                                            
            ***********               ***********           
        ********************     ********************       
     ***************************************************    
    *****************************************************   
   *******************************************************  
  ********************************************************* 
  ********************************************************* 
  ********************************************************* 
  ********************************************************* 
   *******************************************************  
   *******************************************************  
    *****************************************************   
     ***************************************************    
       ***********************************************      
        *********************************************       
          *****************************************         
            *************************************           
               *******************************              
                  *************************                 
                     *******************                    
                         ***********                        
                            *****                           
                              *                             
     

 

~~~
---

## ⚙️ Customization

You can easily alter the look and size of the output shapes by tweaking the following parameters in the loops:

*   **Size:** Decrease the increments (e.g., multiply `col` by `0.05` instead of `0.1`) and scale up the `range()` boundaries to increase the overall resolution.
*   **Characters:** Swap out `"*"` for alternative characters like `"♥"`, `"#"`, or letters to create personalized text art.
*   **Proportions:** Modify the aspect ratio multipliers (`0.1` and `0.15`) to make the heart wider or taller depending on your terminal font settings.
