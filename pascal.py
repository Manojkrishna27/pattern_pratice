import math # this is mathematics libray in python
n=6
for i in range(0,n):
    print(" "*(n-i),end="") # spacing like pyramid structure
    for j in range(i+1):
        value=math.comb(i,j)
        print(value,end=" ")
    print()