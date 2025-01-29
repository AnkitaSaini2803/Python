#  Else part gets printed
for i in range(5):
    print(i)
else:
    print("Sorry Guys")

# Else part doesn't get printed
j=0
for j in range(8):
    print(j) 
    if(j==5):
        break
else:
     print("Sorry Guys")

# Else part gets printed
j=0
for j in range(8):
    print(j) 
        
else:
     print("Sorry Guys")

# example of for loop with else using STRING FORMATTING
for x in range(5):
    print ("iteration no {} in for loop".format(x))
    # print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")


b=0
while(b<6):
    print(b)
    b=b+1
    if(b==4):
        break
else:
    print("Sorry Guys")