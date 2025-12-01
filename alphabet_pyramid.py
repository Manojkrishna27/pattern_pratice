n=5
for i in range(0,n+1):
    print(" "*(n-i),end=" ") # this is for space
    for j in range(0,i+1):
         print(chr(65+i),end=" ")
    print()
   