# 8/1/2025
list=[1,2,3,4,10,23]
print(list)
print(list[:])
print(list[1:-4])
print(list[1:len(list)-2])
print(list[-2:-1])
print(list[len(list)-2:len(list)-1])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]

print(colors[-1])
# print(colors[len(colors)-1])
print(colors[-3])
# print(colors[len(colors)-3])
print(colors[-5])
# print(colors[len(colors)-5])

list_02=['Ramya' ,'Radhika' ,'Ankita' ,'sabha']
print(list_02)
list_03=[1,True,'hello',4]
print(list_03)

string=[2,4,5,1,8,2,True,'hey','hooo','end',5]
print(len(string))
print(string[0:8:2])
print(string[0:9:2])
print(string[2:11:3])

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

if "Yellow" in colors:
    print("Yes")
else:
    print("No")

# LIST COMPREHENSION
List=[i for i in range(10)]
print(List)
Listt=[i*i for i in range(10)]
print(Listt)
Listtt=[j*j for j in range(10) if j%2==0]
print(Listtt)


'''
Yeh toh aise hi hai mene kar ke dekha thaa ,,,ki hoga ya nahi dono ki 
output no aayi hai
if ''' "Blue", "Yellow" ''' in colors:
    print("Yes")
else:                               
    print("No")

if  "Blue" "Yellow"  in colors:
    print("Yes")
else:
    print("No")
'''
