import pdb
def addit(a,b):
    res=a+b
    return res

pdb.set_trace()
x=int(input("enter first number"))
y=int(input("enter second number"))
sum=addit(x,y)
print("The sum of x and y is",sum)
