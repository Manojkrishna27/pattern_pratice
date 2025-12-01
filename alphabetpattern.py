n=5
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=" ") # chr is the character of 65 in ASCII code which is nothing but A 
       
    print()

# for lower case the output like a ab abc we can use lower() or chr(97)
n=5
for i in range(1,n+1):
    for j in range(i):
        print(chr(97+j),end=" ")
    print()