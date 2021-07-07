def my_function(*food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
food={'apple':'red','banana':'yellow'}
my_function(fruits)
my_function(food)

def myfunction():
  pass

#default arguments
def display(a=1, b=2,c=3):
    print('a:', a, 'b:', b, 'c:', c)

print('\nwith no parameters:')
display()
print('with one parameter:')
display(55)
print('with two parameters:')
display(55, 66)

#arguments
print("\n arguments result is")
def arg(*name,**age):
    print("names: ", name)
    print("ages: ", age)
arg('Tim','tom','Jack',first="Welcome",mid="to",last="python")

#recursion
def recursion(k):
  if(k > 0):
    return k +recursion(k-1)
  else:
    return k+2
print("\nResults",recursion(10))

#finding factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))
num=int(input("Enter the number"))
print("The factorial of",num,"is", factorial(num))