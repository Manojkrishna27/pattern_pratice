n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print(4,end=" ")
        elif i==2 or j==2 or i==n-1 or j==n-1:
            print(3,end=" ")
        elif i==3 or j==3 or i==n-2 or j==n-2:
            print(2,end=" ")
        else:
            print(1,end=" ")
    
    print()