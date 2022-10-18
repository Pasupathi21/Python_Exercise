class PyClass:
    def __init__(self, initialValue = 1):
        self.initialValue = initialValue

    def squareValue(self):
        return self.initialValue ** 2

flag = True
userValue = 1
while flag:
    try:
        userValue = float(input("Enter only number: "))
        if isinstance(userValue, int) or isinstance(userValue, float):
            flag = False
        else:
            print('Please entrt the number from 1 to 9')
    except:
        print('Please entrt the number from 1 to 9')
pyObject = PyClass(userValue)
print(pyObject.squareValue())
