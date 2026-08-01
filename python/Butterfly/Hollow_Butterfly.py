n =5 
#upper half
for i in range(1,n+1):
    for j in range (1,i+1):
        if j == 1 or j == i:
            print("*",end="")
        else:
            print(" ", end="")
    print(" " * (2*(n-i)),end="")
    for j in range(1,i+1):
        if j == 1 or j == i:
            print("*",end="")
        else:
            print(" ", end="")
    print()
#lower half
for i in range(n,0,-1):
    for j in range (1,i+1):
        if j == 1 or j == i:
            print("*",end="")
        else:
            print(" ", end="")
    print(" " * (2*(n-i)),end="")
    for j in range(1,i+1):
        if j == 1 or j == i:
            print("*",end="")
        else:
            print(" ", end="")
    print()
    
