# FOR LOOPS                  5/1/2025
# Study about 3 parameters of Range func(stop,start,step) hogya                          
Name="Aaradhya"
for i in Name:
    print(i)

Colors=['Red','Yellow','Green','Pink']
for color in Colors:
       print(color,"\n")
       for j in color:
             print(j,"\n")

#  For Loops using RANGE function     RANGE(start,stop,step)
# start= at which position to start(default value 0)
# stop=at which position to end(required)
# step=incrementation value (optional: default value=1)
for a in range(5):
   print(a,"\n") # 0 to 4 is printed

for a in range(1,50):
   print(a) # 1 to 49 is printed

for a in range(5,50):
   print(a) # 5 to 49 is printed

for num in range(1,20,2):
    print(num)
    
