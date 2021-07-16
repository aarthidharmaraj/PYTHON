import re
p=re.compile('[a-e]')
print("the letters match a-e are : ",p.findall("hai All welcome to regular expression"))

p1=re.compile('\d')
print("It digits found are : ",p1.findall("the time is 6 hours 5 minutes 30 seconds"))

p3=re.compile("\w")
print("Except special characters : ",p3.findall("It includes a-zA-z & numbers 0-9"))


