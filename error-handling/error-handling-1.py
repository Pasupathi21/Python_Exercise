
# Manually raise error 

# Nested structured try  except block
try:
    print('Custom error throw')
    # 100 / 0
    # '123456' / 234567
    raise Exception('USER: Customized error')
except Exception as e: 
    print("Exception block print", e)
finally:
    print('Final block executed 👍👍👍')
    try:
        100 / 0
    except ZeroDivisionError as z:
        print('⚠️ Number should not divied by zero')  
        try:
            float('True')
        except Exception as error:
            print("top of the bottom of the except block::", error)
        except TypeError as t:
            print('⚠️ should pass only number data inside the float or int function')
        except ValueError as v:
            print('⚠️ String is not able to convert number')