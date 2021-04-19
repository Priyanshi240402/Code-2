i=int(input(
    "Enter the no. of element you want"))
n=1
j=1
k=1
while n<=i:
    if n==1:
        print(0,end=",")
        n=n+1
        elif n==2 or n==3:
            print(1,end=",")
            n=n+1
            else:
                m=j
                j=j+k
                k=m
                print(j,end=",")
                n=n+1
