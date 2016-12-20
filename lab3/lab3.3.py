def is_divisible(n,m):
    if int(n)%int(m) == 0:
        return True
    else:
        return False

def is_divisible23n8(n):            
    m="2"
    if (is_divisible(n,2) or int(n)%3==0) and int(n)%8!=0:
        return "yes"
    else:
        return "no"
    




n=(input("Please enter your first integer: "))
if is_divisible23n8(n) is "yes":
    print(n+ " is divisible by 2 or 3 but not 8")
else:
    print("It is not true that " + n + " is divisible by 2 or 3 but not 8")


