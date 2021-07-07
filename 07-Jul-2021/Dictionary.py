ages = {'Jim': 30, 'Jack': 28, 'Kevin': 33}
print(ages)
ages['Rahul']=25
print(ages)
del ages['Jack']
print(ages)

#for avoiding key errors
print(ages.get('Guna'))

person = input('Get age for: ')
age = ages.get(person)

if age:
    print(f"{person} is {age} years old.")
else:
    print(f"{person}'s age is unknown.")

#getting inputs from user
num=int(input("Enter the numbers"))
dic={}
for i in range(0,num):
    name=input("Enter the key name:")
    age=input("Enter the value age:")
    dic[name]=age
print(dic)
for i in sorted(set(dic)):
    print("The sorted value is",i)
#using zip() function
names=['Joe','Jack','Tac']
ages=['4','6','8']
for n,a in zip(names,ages):
    print("{0} is {1} years old.".format(n,a))