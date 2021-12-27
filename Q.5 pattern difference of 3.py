def pattern(n):
        if n==1:
            return 1
        else:
            return pattern(n-1)+3
n=int(input("Enter your number:"))
i=1
while i<=n:
    print(pattern(i))
    i=i+1
# s=pattern(n)
# print(s)
