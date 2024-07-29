#with statement
with open("abcd.txt","w") as f:
 f.write("Hello\n")
 f.write("Hyderabad\n")
 print("is file closed?",f.closed)
print("is file closed?",f.closed)

