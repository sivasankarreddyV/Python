#print the student result using three subjects
s_name=input("enteer a name: ")
maths=int(input("enter maths marks: "))
physics=int(input("enter physics marks: "))
chemistry=int(input("enter chemistry marks: "))

if maths <35 and physics < 35 and chemistry < 35:
    print("student failed")
else:
    print("student passed")
    total=(maths + physics + chemistry)
    print("Total marks is: ",total)
    average=total/3
    print("Average is: ",average)
if average >90:
    print(f"{s_name} is passed in first class: ",total)
elif average>70:
    print(f"{s_name} is passesd in second class:",total)
elif average<60:
    print(f"{s_name} is passesd in third class:",total)
else:
    print("avg pass")
