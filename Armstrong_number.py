number=input("Enter any value:").strip()
leng=len(number)
sum=0
for i in number:
    sum=int(i)**leng+sum
    # print(sum)
if sum==int(number):
    print(f"{number} is an armstrong number")
else:
    print(f"{number} is not an armstrong")