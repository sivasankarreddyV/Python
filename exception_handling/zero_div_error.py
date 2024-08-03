#to print exception handling
try:
    a=20
    b=20
    print(a/b)
except Exception as e:
    print("divison by zero not possible")
else:
    print("divison successful")
finally:
    print('executes no matter what')
)
