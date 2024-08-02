#to print area of rectangle using functions
#without argument without return type
"""def calc_area():
    length=int(input("enter the length: "))
    breadth=int(input("enter the breadth: "))
    area=length * breadth
    print("area is: ",area)
calc_area()
  


#without argument with return type
def calc_area():
    length=int(input("enter the length: "))
    breadth=int(input("enter the breadth: "))
    area=length * breadth
    return area
area= calc_area()
print(f"area is: {area}")



#with argument without return type
def calc_area(length,breadth):
    length=int(input("enter the length: "))
    breadth=int(input("enter the breadth: "))
    area=length * breadth
    print(f" area is: {area}")
calc_area(5,10)




#with argument with return type
def calc_area(length,breadth):
    area=length * breadth
    return area
length=int(input("enter the length: "))
breadth=int(input("enter the breadth: "))
area=calc_area(length,breadth)
print(f" area is: {area}")


