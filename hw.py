def multiply(num):
    temp = len(num)
    prod = 1
    for i in range(temp):
        prod *= num[i]
    return prod

num = (4, 3, 2, 5, -1, -2, 18)
print('Orignal tuple:')
print(num)
print('Multiplying all the tuples: ', multiply(num))

num = (7, 8, 6, 5, 9, -2, 3)
print('Orignal tuple:')
print(num)
print('Multiplying all the tuples: ', multiply(num))