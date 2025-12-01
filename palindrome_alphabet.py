n=5
for i in range(1,n+1):
    print(" "*(n-i),end="") # this is space  for pyramid shape 
    for j in range(i):
        print(chr(65+j),end="") # this will increase like A AB ABC

    for j in range(i-2,-1,-1):
        print(chr(65+j),end="") # this is  decresing part like  BA CBA DCBA 

    print()
 