#tell and seek stateement
f=open("abcd.txt",'w')
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

f=open("abcd.txt",'r')
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())
f.seek(11)
print(f.tell())

