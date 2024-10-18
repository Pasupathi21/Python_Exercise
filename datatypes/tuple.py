# tuple -> immutable and ordered it accepts duplicate values

tuple_val = (0, False, {}, "tuple", {})

for t in tuple_val:
    print(t)
print(type(tuple_val))
print(tuple_val.index({}))