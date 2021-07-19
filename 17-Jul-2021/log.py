import logging
logging.basicConfig(filename="logerror.txt",filemode='a',format='%(asctime)s %(levelname)s-%(message)s',datefmt='%Y-%m-D %H:%M:%S')

for i in range(0,5):
    if(i%2==0):
        logging.warning('warning message')
    elif(i%3==0):
        logging.critical('Critical message')
    else:
        logging.error('Error message')
#built in exception 
res=" "
try:
    a=int(input("Enter a number a: "))
    logging.warning("Check for errors")
    print("The result is",a/0) 
   
except ZeroDivisionError:
    logging.error("number cannot be divided by 0")
    res="Zero division error-Exception handled"
finally:
    print(res)

#user defined exception

class TooLargeError(Exception):
    def __init__(self,mesg):
        self.mesg=print("It is a large number than expected number")
class TooSmallError(TooLargeError):
    def __init__(self,msg):
        self.msg=print("It is a small number than expected number")
num=10
while True:
    try:
        check=int(input("Enter a number for checking"))
        if check<num:
            raise TooSmallError(check)
        elif check>num:
            raise TooLargeError(check)
    except TooSmallError:
        logging.warning("You Entered a small number")
        print("Small Error- Exception handled")
        break
    except TooLargeError:
        logging.critical("You Entered a large number")
        print("Large error-Exception handled")
        break
    else:
        logging.warning("You Entered correct number")
    finally:
        print("The number checked successfully")
