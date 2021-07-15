import re
regex = "^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)$"

#regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$" 
def check(Ip):
    if(re.search(regex, Ip)):
        print("Valid Ip address")    
    else:
        print("Invalid Ip address")
if __name__ == '__main__' :
     
    Ip =input("Enter the IP address to check")
    check(Ip)
 
    # Ip = "110.234.526.124"
    # check(Ip)
 
    # Ip = "366.1.2.2."
    # check(Ip)
    # Ip = "110.234.16.124"
    # check(Ip)