n = int(input("Enter the nuber of diamonds size in row (odd): "))

row = int((n/2)+1)

#Upper half
for i in range (row):
    spaces = " " * (row - i - 1)
    if i==0:
        print(spaces+"*")
    else:
        hollow = " " * (2 * i -1)
        print(spaces + "*" + hollow + "*"  )
#lower half
for j in range (row - 2,-1,-1):
    spaces = " " * (row - j - 1)
    if j ==0:
        print(spaces+"*")
    else:
        hollow = " " * (2 * j -1)
        print(spaces + "*" + hollow + "*"  )
