f1=open('file1.txt','w')
f1.write('Welcome to write file')
f1.write('This is the first line of write file')
f1.close()

f2=open('file2.txt','r')
print(f2.read(10))
print("\nread after 10 characters",f2.read(20))

print(f2.readlines())
f2.close()

with open("file3.txt","wb") as f:
    print("\nFile name",f.name)
    print("\nmode of opening",f.mode)
    print("\nchecking for close",f.closed)
