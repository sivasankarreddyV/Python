# to print name error handling
try:
    a=5
    b=5
    print(a/c)
except Exception as e:
    print("enter the right name of the value")
else:
    print("successful")
finally:
    print('executes no matter what')

