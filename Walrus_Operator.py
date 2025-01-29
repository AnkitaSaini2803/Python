#  24/1/2025
a=True
# a=False
# print(a)
print(a:=False)

'''without using walrus operator                    
food=list()
while True:
    nameFoods=input("Enter the name of food")
    if nameFoods == "quit":
            break
    food.append(nameFoods)
print(food)
'''''

#Using Walrus Operator
food=list()
while name_Food := (input("Enter the food you like:") ) != "Quit" :
  food.append(name_Food)


