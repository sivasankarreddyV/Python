#To read total data from the line

f=open("abcd.txt",'w')
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

f=open("abcd.txt",'r')
line1=f.read()
print(line1)
