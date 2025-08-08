# String Methods                         8-8-2025
# 1. Strip() will remove the whitespaces or characters from the beginning as well as end of the string                                       8-8-2025
x=",,,....pqrs...mango....ji/////" 
print(x.strip("p/q.s,ijr"))                # mango

print(x.strip(".,ij"))                     # pqrs...mango....ji/////

x1=",,,....pqrs...mango....ji..."
print(x1.strip(".,ij"))                    # pqrs...mango

txt=",,,,rrtgbpm...mango,....rrrr"
print(txt.strip("r,"))                     # tgbpm...mango,....


# 2. split()->will convert the string into list of strings
x1=",,,,rr tg   bpm...mango       rrrr"
print(x1.split())


''' 3.    ''.join() is a string method that converts all the items in an 
iterable in a single string
Convert  LIST OF STRINGS  ===>  SINGLE STRING   '''

l='''d MAhGiRTWAb VbgGMnCNKY BVmGVbweFo JrOQXyIQuK RqLzyaMaN'''
print(l.split())

print(l.split( ))

#  print(l.split(''))               ValueError: empty separator