# '''                                        9/1/2025
# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game.

# '''

# print("Namaskaram...Welsome to KBC(Kaun Banega Karod Pati)")
# name=input("Enter Your Name :")
# age=int(input("Enter Your Age: "))
# print("Lets Get Started ...Best of Luck")
# question=int(input("Choose any question from 1 to 6: "))
# match question:
#      case 1:
#             print("Which Planet is Known as RED palnet ?")
#             print("1.Earth")
#             print("2. Mars")
#             print("3. Jupiter")
#             print("4. Saturn")
#             option=input("Choose the correct option out of four given above :")
#             if(option=="2"):
#                   print("Correct,You won 100 Rupees")
#             else:
#                   print("Oops... Sorry,Good Luck Next Time")

#      case 2:
#             print("Who wrote the National Anthem of INDIA ? ")
#             print("1. Rabindranath Tagore")
#             print("2. Bankim Chandra Chattterjee ")
#             print("3. Mahatma Gandhi ")
#             print("4. Subhas Chandra Bose ")
#             option=input("Choose the correct option out of four given above :")
#             if(option=="1"):
#                   print("Correct,You won 100 Rupees")
#             else:
#                   print("Oops... Sorry,Good Luck Next Time")

#      case 3:
#             print("Who was the first President of INDIA")
#             print("1.Jawaharlal Nehru")
#             print("2.Dr. Rajendra Prasad")
#             print("3.Sardar Vallabhbhai Patel")
#             print("4.Dr. B. R. Ambedkar")
#             option=input("Choose the correct option out of four given above :")
#             if(option=="2"):
#                   print("Correct,You won 100 Rupees")
#             else:
#                   print("Oops... Sorry,Good Luck Next Time")
    
#      case 4:
#             print("Which is the largest mammal on Earth?")
#             print("1.African Elephant")
#             print("2.Blue Whale")
#             print("3.Giraffe") 
#             print("4.Hippopotamus") 
#             option=input("Choose the correct option out of four given above :")
#             if(option=="2"):
#                   print("Correct,You won 100 Rupees")
#             else:
#                   print("Oops... Sorry,Good Luck Next Time")

#      case 5:
#             print("Which river is known as the 'Sorrow of Bihar'?")
#             print("1.Ganga")
#             print("2.Kosi")
#             print("3.Yamuna") 
#             print("4.Brahmaputra") 
#             option=input("Choose the correct option out of four given above :")
#             if(option=="2"):
#                   print("Correct,You won 100 Rupees")
#             else:
#                   print("Oops... Sorry,Good Luck Next Time")
#      case 6:
#             print("Which year did India gain independence?")
#             print("1.1945")
#             print("2.1946")
#             print("3.1947") 
#             print("4.1948") 
#             option=input("Choose the correct option out of four given above :")
#             if(option=="3"):
#                   print("Correct,You won 100 Rupees")
#             else:
#                   print("Oops... Sorry,Good Luck Next Time")

# print("Thanks For Participating")

''' WELCOME TO KBC                       12/1/2025'''
print("WELCOME TO KBC")
question=[
      ["Which year did India gain independence?","1945",'1946','1947','1948'],
      ["Which river is known as the 'Sorrow of Bihar'?",'Brahmaputra','Kosi','Ganga','Yamuna'],
      ["Which is the largest mammal on Earth?",'african elephant' ,'Blue whale','Jiraffe','Dog'],
      ["Who was the first President of INDIA",
            'Jawahar Lal Nehru','RabindraNath Tagore','Dr.Rajendra Prasad','Dr.BR Ambedkar'],
      ["Who wrote the National Anthem of INDIA ? ",'Rabindranath Tagore',' Mahatma Gandhi'
       ,'Bankim Chandra Chattterjee','Subhas Chandra Bose ']]

Money=[1000,2000,3000,5000,10000]
money=0
for i in range(0,5):
     Ques=question[i]
     print(f"The Question {i} is for {Money[i]}")
     print(f"{Ques[0]} \nChoose th following answer:\n{Ques[1]} \n{Ques[2]}\n {Ques[3]} {Ques[4]}")
     answer=int(input("Enter the correct answer: "))
     