input_list = [12, 3, 435, 657, 67, 878, 87 ,989, 98]

# filter build-in function in python
# return data if filter condition will satisfied

# return odd nums only
# syntax filter(function, iterable)
filter_list = list(filter(lambda n: n%2 == 1, input_list))

print(filter_list)

# map method 
# syntax map(function, iterable)

# convert odd to even number
even_num = list(map(lambda n: n +1, filter_list))
print(even_num)


# reduce method total all values into one single value
# reduce import from 'functool' module it's not globally available'
from functools import reduce

# syntax reduce(function, iterable)
total = reduce(lambda acc, cu: acc + cu, even_num)
print(total)