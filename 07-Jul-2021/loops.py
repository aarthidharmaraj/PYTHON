users={'tim':'submitted','tom':'notsubmitted','jack':'submitted','rahul':'process'}
# Iterate over a copy
for user,status in users.copy().items():
    if status == 'notsubmitted':
        del users[user]
print(users)
# new collection
sub_users = {}
for user, status in users.items():
    if status == 'submitted':
        sub_users[user] = status
print(sub_users)
#range
for i in range(1,10):
    print("the range is",i)
for n in range(2,20,3):
    print("the range of n is",n)
#break and continue
n = 6
while n > 0:
    n -= 1
    if n==3:
        continue
    if n == 2:
        break
    print(n)
    print('Loop done.')
#nested while loop
a = ['foo', 'bar','hai']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
         print('inside while', b.pop(0))