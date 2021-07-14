import re
s="an example of regular expression search and it checks for and present"
if re.search("and",s):
    print("and is present")

s1=re.findall("a.",s)
for i in s1:
    print(i,end=" , ")

for i in re.finditer("an.",s):
    tup1=i.span()
    print(tup1)
    print(s[tup1[0]:tup1[1]])

ani="cat and ant rat Mat Bat fat pat"
s2=re.findall("[crmf]at",ani)
print("\nThe matched characters are")
for i in s2:
    print(i,end=" ")

print("\nThe matched characters with case sensitive are")
s3=re.findall("[c-mA-M]at",ani)
print(s3)

#replacing
s4=re.compile("[cr]at")
ani=s4.sub("AS",ani)
print("\n After replacing\n",ani)

t="hai 123 welcome to 345"
if re.findall("\d",t):
    print("digits found")
else:
    print("Not found")

str="I.P.S.  I.R.S. F.B.I. AC A.IC "
print("\nthe matched format\n")
print(re.findall(".\..\..",str))

#username checking
name="Aarthi Dharmaraj"
if re.search("\w{2,15}\s\w{3,10}",name):
      print("\n",name,"is a valid user name")
else:
    print("\n",name,"Not a valid user name")

#phone number
phno="91-231-34562"
if re.search("[\w+]\w{2}-\w{3}-\w{5}",phno):
    print("\n",phno,"is a valid number")
else:
    print("\n",phno,"Not a valid number")

#email checking
email="example@gmail.com  exa@sys.com  e@gm.com  eg@gm.c  @gam.com "
s5=re.findall("[\w._%+-]{1,20}@[\w._]{2,20}.[A-Za-z]{2,3}",email)
print(s5)