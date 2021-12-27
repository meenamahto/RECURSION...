def palindrome(n):
    if n[0]==" ":
        return True
    else:
       return n[:]==n[::-1]
n=input("Enter your word:")
a=palindrome(n)
print(a)


