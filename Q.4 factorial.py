def factorial(n):
    if n==1:
        return 1
    else:
        return factorial(n-1)*n
n=int(input("Enter your number"))
b=factorial(n)
print(b)


# a=[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     if type(a[i][j][k])==list:

#                         p=0
#                         while p<len(a[i][j][k]):
#                             b.append(a[i][j][k][p])
#                             p=p+1
#                     else:


#                         b.append(a[i][j][k])
#                     k=k+1
#             else:
#                 b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#         # j=j+1
#     i=i+1
# print(b)
