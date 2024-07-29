#To read all lines into list
f=open("abcd.txt",'w')
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

f=open("abcd.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()

