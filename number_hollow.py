n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or i==1 or j==1 or j==n: # if this condition satisfy it will print 1 else space
            print(1,end=" ")
        else:
            print(" ",end=" ")
    print()