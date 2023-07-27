#  Dictionary

original_dic = {
    "key_1": 1,
    "key_2": 324,
    "key_3": 3
}

print('Original before copy dictionary', original_dic)

copy_dic = original_dic

copy_dic['key_2'] = 2

print('Copy dic', copy_dic)
print('Original dic ', original_dic)

