n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(1,end=" ")
        elif i==2 or j==2 or i==n-1 or j==n-1:
            print(2,end=" ")
        elif j==3:
            print(3,end=" ")
        else:
            print(" ",end=" ")
    print()