# In python class is contains setof method (function) and attributes (variable) 
# methods and 

class TestCls:

    cls_or_static = "THIS IS STATIC VARIABLE"

# __init__ method is like a constructor it will be invoked whenever instantiate the class with new object
    def __init__(self, args = 'Optional'):

        self.args = args if args else None

# class method or functions 
    def first_method():
        return 'My first method'

# create new object from class
test_obj = TestCls()

print(test_obj.cls_or_static)
