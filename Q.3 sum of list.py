def sum_list(lis):
    if len(lis)==1:
        return lis[0]
    return lis[0] + sum_list(lis[1:])

print (sum_list([1, 4, 7, 10]))