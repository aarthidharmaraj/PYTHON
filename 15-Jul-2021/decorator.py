def average(func):
    def get():
        list1=func()
        n=len(list1)
        total=sum(list1)
        avg=total/n
        return avg
    return get

@average
def func():
    list1=[1,2,3,4,5,6,7,8,9]
    return list1

@average
def get():
    list2=[2,3.4,2,5,4,6,7,8]
    return list2

print(func())
print(get())