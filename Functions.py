# Program to find Geometric mean using functions and find which is 
# greater number                            8/1/2025

def findGeometricmean(a,b):
    G_mean=(a*b)/(a+b)
    print("Geomatric Mean is:",G_mean)

def isgreater(a,b):
    if(a>b):
        print("First Number is greater",a)
    else:
        print("Second Number is greater",b)

def isSmaller(a,b):
    pass            

num_1=int(input("Enter the first Number"))
print(num_1)
num_2=int(input("Enter the second Number"))
print(num_2)
# isgreater(10,50)
# findGeometricmean(10,8)

isgreater(num_1,num_2)
findGeometricmean(num_1,num_2)