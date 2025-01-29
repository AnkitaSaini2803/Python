'''Multi-Threading In Python                         26/1/2025'''
import threading
import time
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds
# normal code
# time_before=time.perf_counter()
# func(4)
# func(3)
# func(2)
# func(1)
# time_after=time.perf_counter()
# print(time_after-time_before)

# same code using threads
''''
time_before=time.perf_counter()
t1=threading.Thread(target=func,args=[4])
t1.start()
t2=threading.Thread(target=func,args=[3])
t2.start()
t3=threading.Thread(target=func,args=[2])
t3.start()
t4=threading.Thread(target=func,args=[1])
t4.start()
# time_after=time.perf_counter()
# print("\n",time_after-time_before) it came zero seconds
t1.join()
t2.join()
t3.join()
t4.join()
time_after=time.perf_counter()
print("\n",time_after-time_before) #this time it takes 4 seconds

'''
#using concureent.futures module
from concurrent.futures import ThreadPoolExecutor
def func2():
   with ThreadPoolExecutor() as executor:
       lists=[2,3,4,1,5]
       results=executor.map(func,lists)
       for list in lists:
           print(list)

    #    f1=executor.submit(func,3)
    #    f2=executor.submit(func,2)
    #    f3=executor.submit(func,1)

    #    print(f1.result())
    #    print(f2.result())
    #    print(f3.result())
    
func2()


