#built-in exception
a,b=5,0
try:
    print("Check for errors")
    print("The result is",a/b) 
except ZeroDivisionError as e:
    print("number cannot be divided by 0",e)
finally:
    print("Executed successfully")

#user defined exception
class Error(Exception):
    pass
class TooLargeError(Error):
    def __init__(self,mesg):
        self.mesg=print("It is a large number than expected number")
class TooSmallError(Error):
    def __init__(self,msg):
        self.msg=print("It is a small number than expected number")
num=10
while True:
    try:
        check=int(input("Enter a number"))
        if check<10:
            raise TooSmallError(check)
        elif check>10:
            raise TooLargeError(check)
    except TooSmallError as se:
        print("You Entered a small number",se)
    except TooLargeError as le:
        print("You Entered a large number",le)
    else:
        print("You Entered correct number")
    finally:
        print("The number checked successfully")
