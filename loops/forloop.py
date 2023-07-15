value = [ 100, 423, 325436,  767876,7, 789, 879, 789, 787987]

findMax = value[0]
findMin = value[0]
for item in value:
    if item > findMax:
        findMax = item
    elif item < findMin:
        findMin = item

# print(f'Maximun value is {findMax} and Minimum value is {findMin}')
print(max(value))
print(min(value))