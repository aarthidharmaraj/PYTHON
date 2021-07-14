# #list comprehension
l1=[1,3,2,4,5,3,6,8,3,4,9,6,5,1]
even,odd=[],[]
for i in l1:
    (even.append(i*i) if i%2==0 else odd.append(i*2))
print(even,odd)

evenind=l1[0:][::2]
oddinde=l1[1:][::2]
even2=[a*b for a,b in zip(evenind,evenind)]
odd2=[a*2 for a in oddinde]
print(even2,odd2)

list_comp=[(i**2) for i in l1 if i%2==0]
list_comp1=[i*2 for i in l1 if i%2!=0]
list_com=[list_comp,list_comp1]
print(list_com)