# *args - packing positional arguments
# **kwargs - packing keyword arguments

def test_fun(*args, **kwargs):

    # args --> return bunch of arguments with tuples data type
    print('args :', type(args))
    print(args)

    # kwargs --> returns bunch of arguments with dictionaries format {key: values }
    print('kwargs :', type(kwargs))
    print(kwargs)


test_fun(
    'arg_1',
    'arg_2',
    'arg_3',
    'arg_4',
    kw_1="kwargs_one",
    kw_2="kwargs_one",
    kw_3="kwargs_one",
    kw_4="kwargs_one"
)