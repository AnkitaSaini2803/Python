'''27/1/2025'''
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import requests

def Download_file(url,name):
    info=requests.get(url)
    open(f"FILES/file{name}.jpg","wb").write(info.content)
    # with open(f"FILES/file{name}.jpg", "wb") as file:
        #  file.write(info.content)
if __name__== "__main__":
 url="https://picsum.photos/2000/3000"

#  Processes=[]
#  for i in range(20):
#     #returns a process that runs the target function with specified arguments
#     p= multiprocessing.Process(target=Download_file,args=[url,i])
#     p.start()
#     Processes.append(p)
    
#  for p in Processes:
#     p.join()
 
 with ProcessPoolExecutor() as executor:
    l1=[url for i in range(31)]
    l2=[i for i in range(31)]
    results=executor.map(Download_file,l1,l2)
    for result in results:
      print(result)
   

