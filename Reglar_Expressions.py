import re
'''Searching for a pattern'''
expression=r"[A-Z]+og"
text='''Ankita is a good girl
         she has pet Dog whose name is rommy
         rommy is her favourite pet
         Fog is there , Mog'''
result=re.findall(expression,text)
print(result)

'''Replacing a pattern'''
new_text="This cat is his cat"
expression2=r"[a-z]+at"
result1=re.sub(expression2,'Dog',new_text)
print(result1)