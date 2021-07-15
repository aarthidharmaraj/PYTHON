f=lambda a,b:a*b
print("\nMultiplication of two numbers is",f(2,5))

#using filter
ls=[1,2,3,4,5,2,4,7,8,9]
even=list(filter(lambda n:n%2==0,ls))
print("\n The even numbers from the list are",even)

#using map

m=list(map(lambda a:a*2,even))
print("\n result is",m)

#using reduce
from functools import reduce
num=[2,4,6,8,3,2,1,4,9,12,3,10]
max=reduce(lambda a,b:a if a>b else b,num)
print("The result after reducing is",max)

#using accumulate
from itertools import accumulate
max2=list(accumulate(num,lambda a,b: a+b))
print("The result of accumulation is",max2)
max1=list(accumulate(num,lambda a,b: a if a>b else b))
print("The result of accumulation is",max1)