def pattern(number):
    if number == 1:
        return 10
    elif number % 2 == 0:
        return pattern(number - 1) + 1
    else:
        return pattern(number - 1) * 10
a=int(input("Enter your number:"))
i=1
while i<=a:
    print(pattern(i))
    i=i+1
# b=pattern(a)
# print(b)

