# 5/1/2025                          PAUDI VALA SHIV MANDIR,HIMACHAL PRADESH
# Match case statement(match variables value with all patterns(like:case 0) until one
# is matched and in case no case is matched default case will get executed)

variable=int(input("Enter the vaue of variable"))

match variable:
    case 0:
        print("Value of variable is 0")
    case 3:
        print('Value of variable is 1')
    case 5:
        print('Value of variable is 5')
    case _ if variable<5:
        print("Value of variable is greater than 5")
    case _ if variable>=15 and variable<=30:
        print("The value lies between 15 and 30")
    case _:  #this is default case it will only be matched if above cases are not matched
        print(variable)
        print("Sorry, you miss the oppourtunity.Try next time")

