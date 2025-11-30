n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n: # i for first and last row and j for printing star for first and last column
            print("*",end="")
        else:
            print(" ",end="") # this is for space if the if block conditions fail 
    print()