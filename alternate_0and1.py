n=5
for i in range(1,n+1):
    start=i%2 # row will modulus by 2 REMEMBER 1%2 =1
    num=start # num is a storage of start
    for j in range(1,i+1):
        print(num,end=" ")
        num=1-num
    print()