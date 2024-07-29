#to read data line
f=open("abcd.txt",'w')
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

f=open("abcd.txt",'r')
line2=f.readline()
print(line2)
