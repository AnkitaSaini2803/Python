import time                      #24/1/2025
'''time.time()'''
t1=time.time()
print(t1)

print("Hey today is 24 January 2025")
print('Time before: ',time.time())

'''time.sleep()'''
time.sleep(3)
print("The output was few seconds delayed")
print('Time After:',time.time())

''''''

def using_forLoop():
    for i in range(100):
        print(i)
    
print('\n')

def using_whileLoop():
    i=0
    while(i<100):
        print(i)
        i=i+1

t2=time.time()
print(t2)
using_forLoop()

print(time.time()-t2)
using_whileLoop()


'''time.strftime()'''
Current_T=time.localtime()
timing=time.strftime("%H : %M : %S",Current_T)
print(timing)