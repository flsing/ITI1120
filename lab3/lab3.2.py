
def is_divisible(n,m):
    if int(n)%int(m) == 0:
        return True
    else:
        return False


n=(input("Please enter your first integer: "))
m=(input("Now please enter another integer: "))
if is_divisible(n,m) is True:
    print(n+ " is divisible by " +m)
else:
    print(n+ " is not divisible by " + m)
    


