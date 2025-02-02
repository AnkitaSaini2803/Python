import math
list=[23,2,4,3,1,9]
def check_PRIME(number):
    if number<=1:
        print(f"{number} is not prime")
        return
    for i in range(2,int(math.sqrt(number))+1):
        if number % i==0:
            print(f"{number} is not prime")
            return
    else:
            print(f"{number} is prime number")
            return
for j in list:
    check_PRIME(j)

