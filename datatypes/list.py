# list -> ordered, changeable and accepts duplicates

list_val = [1, 32 ,4,546, 556, 6, { "key": "Key value" }]

# print(list_val[:: -1])
c_list_val = list_val.copy()
c_list_val[-1]["key"] = 1000
print(list_val)
print(c_list_val)
# print(type(list_val))