
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-1)+fibo(n-2)
n=int(input("Enter your number:"))
i=1
while i<=n:
    print(fibo(i))
    i=i+1

# for i in range(1,n+1):
#     print(fibo(i))