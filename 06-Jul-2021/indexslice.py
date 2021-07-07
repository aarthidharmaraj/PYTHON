a=input("Enter a number")
print(a)
#For entering set of numbers
print("Enter numbers")
b=input().split()
print(b)
#to integer type
print("Enter numbers")
b=list(map(int,input().split()))
print(b)

#operators
a=2;b=3
an=a&b
ar=a^b
print("The result is",an,ar)
print(a is b)

#operator Precedence
c=d=3
oper=a+b**2^b*c//d
print(oper)

#Fibanocci
a,b=0,1
while a<10:
    print(a,end=',')
    a,b=b,a+b

#string concatenation
'welcome to python''programming language'

first='wel'
combine=first+'come'
print(combine)

#indexing
i='python programming'
print(i[6])
print (i[10])
print(i[-3])

#slicing
print(i[:2])
print(i[2:])
#[start: end: step]
print(i[2::2])

#changing string
print('Java'+i[4:])