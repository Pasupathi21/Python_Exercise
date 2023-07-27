# Collection data type have multiple type of data in single variable

# List data type

var_list = [{}, False, False, 'String', 232534, 21432457.243357]

print(var_list)


# ###### dir() function list available methods for the data type

#  ######## help() function describe how to use the function

# Set data type
# Set data automatically removes the duplicates

var_set = { False, False, 'String', 243567, 3547.24325}
print('Set data', var_set)
print('var_set', var_set.pop())
print(len(var_set))

# print(dir(var_set))
# help(var_set)
# Tuples data type

var_tuple = ( False, False, 'String', 'String', 243567, 3547.24325 )
print('Tuple data', var_set)
print(len(var_tuple))

# Dictionary
dic_data = {
    "key_one": 'One',
    "key_two": 'Two',
    "key_three": 'Three'
}

print('dic_data', dic_data)
dic_data['key_three'] = True
print('value changed', dic_data)