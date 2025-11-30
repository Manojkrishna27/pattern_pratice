# diamond
row =5 # upper pyramid
for i in range(1,row+1):
    print(" "*(row-i),end=" ")
    print("* "*i) # this space is important

rows=4 # lower pyramid
for i in range(rows,0,-1):
    print(" "*(rows-i),end=" ")
    print(" *"*i) # this space is important
# together they form diamond
