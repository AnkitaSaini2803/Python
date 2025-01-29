''' 15/1/2025'''
file=open('file.txt','r')
text=file.read()
print(text)
file.close()

# file=open('New_file.txt','w')    #new file created

file=open('New_file.txt','w')
text=file.write('Hello World I am learning File Handling in Python')
print(text) # Print the number of characters written to the file
file.close()
'''The no. of times i will run this code this line will be appended(written)
there same no. of times
'''
file=open('New_file.txt','a')
output=file.write("\nMy Name is Ankita Saini")
file.close()

''' this will override the code and print this new line
'''
file=open('New_file.txt','w')
output=file.write("\nMy Name is Ankita Saini")
file.close()

'''
Now, everytime you open a file you need to close it everytime
so to avoid writing close 
you can also use 'with' statement to automatically close a file when 
you are done with that file
'''
with open('file.txt','a') as file:
    
    file.write("\nPineapple very good veryy nicceee\n")


f=open('file.txt','r')
outpur=f.read()
print(outpur)
f=open('file.txt','r')
result=f.read(5) #Read the next 5 bytes
print(result)
f.close()

f=open('file.txt','r')
result=f.readline()
print(result)

f = open('file.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

'''seek() function'''
with open('New_file.txt','r') as file:
    r1=file.seek(7) # Move to the 7th byte in the file
    result=file.read(10) # Read the next 10 bytes
    print(result)

'''Tell() function'''
with open('file.txt','r') as f:
    line=f.read(10)
    print(line)
    current_position=f.tell()
    print(current_position)      #10
    
'''Truncate() function if you want to truncate the file to a 
   specific size, you can use the truncate function.'''
with open('New_file.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('New_file.txt', 'r') as f:
  print(f.read())