# Tuples unpacking

print('-------------Tuples unpack ------------------s')
listData, dicData, setData = (
    [2345, 98765, 23, 7665, 3567],
    {
        "key1": '234567',
        "Key1": True
    },
    {234, 6, 43567, 4567, 8765, 4567}
)


print(listData, dicData, setData)

print('-------------List unpack ------------------')
one, two, three, four, five = listData
# print(isinstance(listData) == object)
print(one, two, three)


# Set un packing
print('-------------Set unpack ------------------')
s1, s2, s3, s4, s5 = setData
print('S1', s1)