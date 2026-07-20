n = 5 
# upper half of butterfly  (two mirrored right-angle triangle)
for i in range(1, n+1):
    print("*" * i + " " * (2*(n - i))+ "*" * i)    

#lower half of butterfly  (two mirrored right-angle triangle)
for i in range(n,0,-1):
    print("*" * i + " " * (2*(n - i))+ "*" * i)    