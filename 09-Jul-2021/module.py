import cardetails
#import builtins
c=cardetails.car("AAR",2021,100000)
print("Car owner name from module:",c.names())
print("Car bought year from module:",c.years())
print("Car price from module:",c.prices())

from cardetails import *
advance=int(input())
base_price=int(input())
c.cal(advance,base_price)

from cardetails import years as y

from module2 import *
mod2()
mod2_func2()