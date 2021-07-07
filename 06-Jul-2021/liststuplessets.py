a=['violet','indigo','blue','green','yellow','orange','red','green','blue']
print('The length of a is',len(a))

#net lists
b=['hi','aar','thi']
m=[a,b]
print(m)
print(m[0][2])

#methods
print(a.index('indigo'))
print(a.index('blue',3))
a.append('welcome')
print('after appending',a)
a.insert(2,'sai')
print('after inserting',a)
a.remove('blue')
print('Removing results',a)
b.sort()
print('Sorting of a',b)
a.reverse()
print('Reverse of a is',a)

#comprehensions
square=[x**2 for x in range(10)]
print(square)
from math import pi
value=[str(round(pi,i))for i in range(1,6)]
print(value)

#tuples
tu=123,342,'hi','welcome'
print(tu)
print("3rd index of tu is",tu[3])
#net tuples
pl=1,2,3455,'python'
tuple=tu,pl
print("combined value is",tuple)
#tuple[0]='hi'

#sets
colours={'violet','indigo','blue','green','yellow','orange','red','green','blue'}
print("Afetr eliminating duplicate entries",colours)
#test for presence
print('after testing','yellow' in colours)
print('After testing','pink' in colours)