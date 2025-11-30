# this is nothing but we need to reverse the butterfly logic 
n=5
for i in range(n,0,-1): # this loop  is for reverse
    print("*"*i+" "*2*(n-i)+"*"*i)

for i in range(1,n+1):# this is for forward
    print("*"*i+" "*2*(n-i)+"*"*i)