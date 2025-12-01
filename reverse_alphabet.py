n=5
for i in range(1,n+1):
    start=n-i # it gives 4,3,2,1
    for j in range(start,n):
                                # remember you need to know ASCII code for this
        print(chr(65+j),end=" ") # chr(65) is A when we add 4 to chr(65) it will becomes chr(69) which is equal to E 
    print()