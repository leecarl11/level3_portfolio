#import random
# #print("this is my file")
# #message = "how are you"

# greeting = "Hello everyone!"
# #print (message)
# #print(1234 + 20)
# #print(12.34 + 10)
# #print(True)
# #print(False)
# #print(None)

# #print(len(greeting))
# #print(greeting[1])
# #print(greeting[-1])
# #print(greeting.upper())
# #print(greeting)

# print("this is a string for displaying characters")
# print("1234")#this is a string 
# print(1234+1)#this is an integer/whole number
# print(12.45)#this is a float
# print(True)#boolean data value
# print(False)#boolean data value
# print(None)#blank/null data

# print(len(greeting))
# print(greeting[0])
# #targeting the last character
# #index positioning/character positioning, this can be used on other data types as well
# print(greeting[-1])
# #the dot notation is another way of finding information, this is another way for python to access data's specific function.they work as print(greeting is(object).upper is(method)(these brackets are always needed because methods are of the data type specific function, and all functions are brackets even if nothimg goes in them)),what is the thing we are doing it to and what are we doing.
# print(greeting.upper())
# #using the method .upper has forced everything in the string that can change case to change case to upper case,.upper works on an object/strings even if its a variable and then performs a function and in this case it was swapping any letter it can to a capital. there are some other methods there are alot of string methods exaples include ;lower()(lower case letters),capitalized()capitalize the first character and if any letter is in uppercase it will make it lowercase),count()(string.count(string, start_index,end_index)),find()(String_Value.find(Substring, Starting_Position, Ending_Position)),replace()(string.replace("old string","new string", count)),strip()(string.strip(characters))(this removes spaces at the beginning and at the end and also beginning and end characters in a string)
#methods that we have looked at are built into python and to access more methods in python we import libraries
# print(greeting)
# print("HELLO".lower())
# print("hello EVERYONE. THIS is innovate!".capitalize())
# print("hello EVERYONE. THIS is innovate.".count("hello"))
# print("This quick brown fox fox fox".count("Fox"))
# print("TheT quick brown fox".find("T"))
# print("The quick brown fox".replace("fox", "frog"))
# print(len("The quick brown fox            "))
# print(("The quick brown fox").strip("fox"))
# stripped="The quick brown fox                 ".strip()
# print(len(stripped))

#LIBRARIES
#libraries which is a collection of methods,methods that we have looked at are built into python and to access more methods in python we import libraries,(random library is a collection of methods used to generate numbers)
#an example of a library is the random library which gives us access to many methods that do the difficult job of generating random numbers for us.we can import more methods depending on what you want.
# print(random.random())
# #this generates a random number between 0 and 1, including 0 only.
# print(random.uniform(1,10))
# #this generates a random number between 1 and 10, inclusive.
# print(random.randint(1,10))
# this genrates a random integer between 1 and 10, inclusive.
# not having access to methods means libraries are not imported,by using import we can get a lot more methods in python and this saves time from having to write your own code to do tasks 
# random is a library in python which you must import if you want to use the functionality in python.
# random, uniform, randit are methods in the random library we wrote them as object.method brackets.
# random.random()
#random.uniform(1,10)
#random.randint(1,10)
#they may or may not need parameters
#import random imports every single methods in the random library
# import random

# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,10))

# #can be written instead as 
# from random import random, randint, uniform

# print(random())
# print(uniform(1,10))
# print(randint(1,10))

#VARIABLES
#snake_case is a naming convention used in python 
# my_name="Debbie"
# my_age=40
# student=False

#print(my_name,my_age,student)
#print("Hello my name is", my_name)
# print("Hello my name " + my_name)
#.format method used to be the best practise, uses{} as placeholders and data is filled in their place based on orders of args in  the method 
#print("Hello my name is {} and i am {} years old".format(my_name,my_age))
#using the .format method to fill in the sentence for the place holder 
#.format allows us to put place holders into a string and then fills in the spaces of those place holders at the end, so those place holders are curly brackets or braces{}, these are used as place holders in python  
#print(f"Hello my name is {my_name} and i am {my_age} years old")
#the f string is the new best practice

#= this is an ASSIGNMENT OPERATOR which assigns a value to a variable

#MATHEMATICAL/ARITHMETIC OPERATORS
# print(1+2)
# print(3-2)
# print(3*3)
# #exponential
# print(3*3*3)
# print(6/2)
# #modulus/remainder,does the division and returns a remainder 
# print(16%3)

# balance=100
# print(balance)
# amount=200

# balance=amount+balance
# #does exactly the same thing as above
# balance +=amount
# print(balance)

# answer=input("What is your name?")
# print(answer)

#input function gives a user a prompt and to take a response back from the user.save it to the variable,input is always a string 
# name=input("What is your name? ")
# print(name)
# #input is always a string and not an integer

#if else
# #here we set out situation for our code to compare and the result of that comparison could result in the code indented below being executed.its important where the dents are in python it relies on those indents for some instructions
# #this is the most basic form of an if statement
# music = "classical"
# if music.upper()== "classical":
#     print("Oh no its classical music again")
# elif music == "no music":
#     print("Ahh, Peace and quiet!")
# elif music == "my chemical romance":
#     print("Debbie, stop crying") 
# #else doesn't need a comparison because it fits into any other situation as well
# #else is any other situation do this     
# # else:
# #     print("Nice and noisy.")   
# # print("That was an if statement")
# # #getting out of the indentation of comparison in order to go into another comparison 

# DIVISIBLE OPERATOR
# #MODULUS OPERATOR%
# #there is no if for comparison, this is just a situation
#COMPARISON OPERATORS==
# print(10%2 == 0)
# print(10%3 == 0)

#this runs based on a condition
#ASSIGNED OPERATOR=
# num = 10
# num2 = 20
#the if statement does the first statement that's true and then goes down to carry out the next executable code. 
# if num > num2:
#     print(f"{num} is bigger")
# elif num2 > num:
#     print(f"{num2} is bigger")
# else:
#     print("Both are equal")

# place = "MCR"
# weather = "Cloudy"

#AND OPERATOR
# #AND are logical operators lets us link two conditions into one line of the if statement,either sides of the and comparison most be true for the whole thing to be true,both sides of the statement most be true 
# if place == "MCR" and weather == "Cloudy":
#     print("Check again")
# elif place == "MCR" and weather == "Rain":
#     print("Obvious")
# else:
#     print("wait, it isn't raining?")
#when we use the and operator true and true is true
#true and false is false
#false and false is false

#OR OPERATOR
#OR is another logical operator,either sides of the statement can com back as true and it's enough to satisfy the whole statement
#when we use the or operator
#true or true is true 
#true or false is true
#false or false is false
# day = "Monday"
# bank_hol = False
# if day == "Saturday" or day == "Sunday" or bank_hol:#if and elif can be combined together if they result in the same situation, they can be combined in the or operator to make our code more efficient.we don't have to be comparing the same thing
#     print("A day off!")
# else:
#     print("Off to innovate we go")

#FUNCTIONS
#they are things that have commands like behind them, we give functions data and they process it and return it back to us in some way,the print or any other function is to take what we put in the bracket process it and put it into the terminal,typing print ,input or any other function is calling that function and that's simply just using it's name      
#A METHOD is a function that works on a specific object and then returns an output
#we can create functions to do specific processesin our programs print,input functions already exists, we can write our own functions to create processes we want to do again and again,when we write our own functions we need to give the program a heads up that this isn't a function that already exists this is a function we are defining and so we use the key word def ,we also give our function a logical name most be in snake_case all in lower case _ and brackets
#between the def and print line is the definition of the function and it's what is instructing our program
#calling the function name that was created and this process will occur.
#functons are used to repeat processes again and again
def light_switch():
    print("Who turned out the lights?")#action we want the function to take 
light_switch()
#installing parameters amount and aacnum
def cash_withrawal(amount, accnum):
    print(f"Withdrawing {amount} from account {accnum}")#action we want the function to take 
cash_withrawal(300, 50449921)


# while num < 10:
#     num +=1
#     print(num)

# my_num = 13
# comp_num = random.randint(1,50)

# while my_num != comp_num:
#     print(f"The numbers {my_num} and {comp_num} do not match")
#     comp_num = random.randint(1,50)

# print(f"The numbers {my_num} and {comp_num} do not match")
#print(10%3==0)


    
# day = "Friday"
# bank_hol = False

# if day == "Saturday" or day=="Sunday" or bank_hol:
#     print("A day off")
#     #print("It's the weekend!")
# else:
#     print("Off to innovate we go")

# def light_switch():
#     print("Switching the lights")
    
# light_switch()

# def cash_with (amount, accnum):
#     print(f"from you account you have withdrawn {amount} from account {accnum}")
# cash_with(300, 12345678)

# fav_songs = ["the foundation of decay - my chemical romance ", "Pandemonium - killing joke", "Jigsaw falling into Place Radiohead"]

# print(fav_songs)

# fav_games = ["cypherpunk", "watch dog", "grand theft auto"]

# print(fav_games)

# fav_songs[1] = "Adam's song blink 182"
# print(fav_songs)
# print(len(fav_songs))
# fav_songs.append("Army of me - bjork")
# print(fav_songs)
# #pop will get rid off an item from a list
# fav_songs.pop(2)
# print(fav_songs)

# print(fav_song[0])
# print(fav_song[1])
# print(fav_song[2])

#a list is iterable
# fav_songs = ["the foundation of decay - my chemical romance ", "Pandemonium - killing joke", "Jigsaw falling into Place Radiohead"]
#for loops
# #i is index
# for i in fav_songs:
#for i in range(0,10,1)
#     print(i)
# for i in range(2,10,2):
#     print(i)
#start/stop/step   
# for i in range(10, -1,-1):
#     print(i)


