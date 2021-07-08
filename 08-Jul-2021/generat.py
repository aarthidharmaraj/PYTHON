#iterators
nums=[2,3,4,5,3,6,8,8,9,10]
it=iter(nums)
print(it. __next__())
print(next(it))

#generators
def ten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
values=ten()
for i in values:
    print(i,end=",")
