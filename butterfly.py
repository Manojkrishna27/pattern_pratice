n=5
for i in range(1,n+1): # this is for upper part
    print("*"*i+" "*(2*(n-i))+"*"*i) 
for i in range(n-1,0,-1): # this is for lowwer part
    print("*"*i+" "*2*(n-i)+"*"*i)

# understand the print logic the butterfly is very easy