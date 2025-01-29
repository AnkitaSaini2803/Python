# BREAK
for i in range(50):
     if(i==11):
        break
     print(i)
    #  print("10 * ",i,'=',10*i)
     print("10 * ",i+1,'=',10*(i+1))
    #  print("10 * ",i+2,'=',10*(i+2))
print('Loop ke bahr aa jao')  

# BREAK WITH FOR LOOP
for iter in range(1,30,1):
    print(iter,"Misipii")
    if(iter==20):
     break
else:
    print("HEY misisipii")
print("Thank You")




# CONTINUE
for j in range(12):
    if(j==10):
        continue
    # print("2 * ",j,'=',2*j)
    print("2 * ",j+1,'=',2*(j+1))

# CONTINUE WITH FOR LOOP
for item in range(1,30,1):
    print("Misipii")
    if(item==20):
     continue
else:
    print("HEY misisipii")
print("Thank You")


for iteration in [2,3,4,6,8,1,0]:
   if(iteration%2!=0):
      continue
   else:
      print(iteration)
    