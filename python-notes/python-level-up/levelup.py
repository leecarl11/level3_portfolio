#CONVERTING DATA TYPES

#METHODS are things we do to our data
#PROPERTIES are things about our data 

#are all methods, these are built in functions that convert one data type to another
# int()#this converts to integer data type
# float()#this converts to floating point data type
# str()#this converts to string data type
#converting data types is called casting 
# int(5.4)Floating point
# int("54")String 

# print(int(5.6))
# print(float("seven"))
# print(round(5.9))

# balance = 100
# deposit = int(input("how much do you want to deposit?"))

# balance +=deposit
# print(f"you have {balance}")

# print("what is your name?")
# name = input()

# if name:
#     print(f"welcome {name} to innovate!")
# else:
#     print("you did not submit a name")
    
# day="Monday"
# bank_hol = True

# if day =="Saturday" or day=="Sunday" or bank_hol:
#     print("Yay a day off")
# else:
#     print("Off to innovate we go")
    

#global variable
# light = False
# def light_switch():
#     global light
#     if light:
#         print("Whoa! its bright in here")
#         #local variable
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True
        
# light_switch()
# light_switch()    
# light_switch()
# light_switch()  
#[] lists can be changed

# even_nums =[2,4,6,8,10]
# even_nums.append(12)
# even_nums.insert(0,0)
# print(even_nums)

# #()tuples can't be changed once made
# odd_nums=(1,3,5,7,9)
# odd_nums.append(11)
# print(odd_nums)

#slice Notation
# fav_songs = ["the foundations of decay - my chemical romance", "Pandemonium - killing joke", "jigsaw falling into place radiohead", "army of me _Bkorks"]
# #start:stop:step
# print(fav_songs[1])#this is index position - it is the start value
# print(fav_songs[1:2:1])#this is actually whats happening -starting short of 2,and stepping by 1 at a time
#create an integere data type 
# print (int(5.4))#Floating point this is converted to an integer
# print (str("54"))#String this is converted to a string 
# print(int(round(5.9)))#this rounds off the numbers 
# #the type function tell you what data type that is
# #int 54, type int or any other conversion type,print type 
# print(type(int(54)))
# print(int("seven"))
#what input takes from the user is always a string even if we type in numbers, which means we can become a little bit limited with the thing we can do with it.

# balance = 100
# deposit = float(input("How much do you want to deposit? "))
# balance +=deposit

# print(f"You have {balance}")
#Comparison operators 
#Falsy values are 
#Empty strings "", empty list, empty tuples, empty, empty dictionaries
#integer values 0
#Floating point value 0.0
#The value false itself and the data type none
#Everything else is Truthy 

# print("What is your name?")
# name = input()

# if name:
#     print(f"Hello {name}, Welcome to innovate!")
# else:
#     print("You did not submit a NAME! home boy.")
#this good for examples like the code above from earlier, where it doesn't matter what the data is just as long as some data comes through we can let a process happen,it's doesn't matter what they type in as a name as long as they type in something as long as name comes back as TRUTHY then that process can carry 
# #before we do a direct comparison we were looking for something to equal something, and the whole statement to be evaluated as true, what we are lookping for in this case is if name returns us something that is considered a truthy value, which is anything that isn't falsy, empty strings are falsy,we need to look for a direct comparison(logical operators)
    
# day="Monday"
# bank_hol = None

# if day == "Saturday" or day=="Sunday" or bank_hol:
#     print("Yay a day off")
# else:
#     print("Off to innovate we go!")
#we also have the not operator we are aware of the does not equal to, comparison operator!= which basically means 'not eqaul to'there is also the not operator,what the 'not'operator does is to flip the value of the boolean, so if we print not true it will flip it and print false, if we say print not false it's going to flip it and it's going to be true, this can be very handy for us to write conditions in 

# print(not True)#expected:False
# print(not False)#expected:True

# allowed=["Andy", "Bob", "Carol", "Debbie", "Dhriti"]#using the not operator to determine who is coming in and who isn't coming into the club
# name=input("What is your name? ")

# while name not in allowed:
#     print("Your name isn't on the list")
#     print("Try again")
#     name=input("What is your name? ")

# print(f"You are welcome {name}," " you can come in. ")

# print("What coat is always wet when you put it on? ")
# answer=input("answer here: ")

# if "paint" in answer:
#     answer=input("what is the answer? ")
#     print("you are right")
    
#TRY/EXCEPT
#these statements have very similar syntax to if/else statements, but they are there to help you catch any errors without your program breaking 
#When a code siezes it's called a fatal error,there is no error message the program did what it was told to do 
def add_up():
    num1 = input("What is the first number you did like to add up? \n")
    num2 = input("What is the second number you did like to add up?\n")
#converting the num1 and num2 into integers and then the program will be able to add the 2 numbers 
#TRY EXCEPT BLOCK has been included in this function
    try:#try and run the program if there isn't any fatal error 
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}!\n")
        print("you are right!\n")
        
    except:#this will run if what we are trying to do will cause a fatal error, also writing our own error message with this code make our own situation 
        print("\nERROR: please input only numerical values.\n")#this will run without raising a fatal error
    print("******************************\n")
    print("please try again\n")
    add_up()#this calls the function again and gives the user another chance at trying,and this helps for error handling also, giving the user safety net as possible 
add_up()#try and except allows us to write our error handling,fulfill that for us 