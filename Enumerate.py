'''13/1/2025'''
# marks=[94,92,97,68,97,99,59]
# index=0
# for i in marks:
#     print(i)
#     if(index==4):
#         print("Hey how r u")
#     index+=1

marks=[94,92,97,68,97,99,59]
for index,i in enumerate(marks):
    print(i)
    if(index==5):
        print("Hi,Ankita")

for index,i in enumerate (marks,start=5):
    print(i)
    if(index==5):
        print("Hey, how can i help you?")