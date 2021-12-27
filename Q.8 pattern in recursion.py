def func(n):
    if n==1:
        print("-")
        return
    print("-"*n)
    func(n-1)
    print("-"*n)

func(3)





# in loop

def nes(n):
    if n==1:
        return "-"
    return nes(n-1)
def ness(a):
    if a==3:
        return "-"
    return ness(a+1)    
a=((int(input("Enter your number:"))))
while a>1:
    i=1
    while i<=a:
        print(nes(i),end=" ")
        i=i+1
    print()
    a=a-1
n=3
i=1
while i<=n:
    j=1
    while j<=i:
        print(ness(i),end=" ")
        j=j+1
    i=i+1
    print()