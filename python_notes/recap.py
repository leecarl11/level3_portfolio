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
#ASSIGNMENT OPERATOR=
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
# def light_switch():
#     print("Who turned out the lights?")#action we want the function to take 
# light_switch()
#amount and accnum are parameters and when called the explicit data we give them are called arguments
# def cash_withrawal(amount, accnum):
#     print(f"You have Withdrawn  {amount} from account {accnum}")#action we want the function to perform
# cash_withrawal(300, 50449921)#300 is the argument that will fill the parameter amount and 50449921 fills the parameter accum.

#LISTS
#lists are written with sqaure brackets and are iterable
# coffee_order = [
#     "Alex - Cortado", "Ben - Latte", "Charlie - Whatever's new"
# ]#this could be for any data types but in this instance we are using strings
# # print(coffee_order)
# print(coffee_order[2])#this is index position this gives the item on the list rather than character position in the strings 
# fav_songs = [
#     "The foundations of decay - my chemical romance ", "Pandemonium - Killing Joke", "Jigsaw Falling in Plcae Radiohead"
# ]
# print(fav_songs)

# # fav_games = [
# #     "watchdogIV", "need for speed", "cyberphunk2077"
# # ]
# # print(fav_games)

# print(fav_songs[1])#index position this goes for the whole item in a list 
# #replacing and re-assigning a new song to the list  
# fav_songs[1] = "Adam's dong - Blink 182"
# print(fav_songs)
# #using the len to find out how many items are in the list
# print(len(fav_songs))
# #the append method is used to add item to the end of the list
# fav_songs.append("Army of Me - Bjork")
# print(fav_songs)
# #. pop is the method used to remove the last item from a list
# #without parameter it will default and get rid of the last one  in the list of items, a parameter can be used just put and index paramater as an argument you don't need the square bracket because it already knows to take the integer as an index position, and it will get rid of the index position, there are many ore lists methods
# fav_songs.pop(2)
# print(fav_songs)

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

#LOOPS
# print(fav_song[0])
# print(fav_song[1])
# print(fav_song[2])
#ARRAY is any kind of collection in python,a list ,set ,dictionary and tuple are all arrays, a list is a kind of array. in python lists are iterable which means they can be used as sequence it can be iterated through(run through)one way to do this is for loop,LOOPS allow to repeat actions and a FOR LOOPS allows us to repeat actions for as many things they are  in the things we can sequence through, so we need a range of things to sequence through like a list of items
#to be able to print a list individually one way this could done is by using FOR LOOPS
# fav_songs = ["the foundation of decay - my chemical romance ", "Pandemonium - killing joke", "Jigsaw falling into Place Radiohead"]

#FOR LOOPS allows us to repeat actions for as many things they are in the things we can sequence through, so we need a range of things to sequence through like a list of items,because a list is iterable, the loop stops when i has no value to be and there is no other index position in that list,for loop is used for completing sequence specific amount of times, that amount of times being how many things there are in the sequence 

#using the keyword for to start a for loop, for initiates the loop,and then we make a new variable for i in and then we define the thing we want to sequence through fav_songs (list)which is the list to be ierated through, this loop will now run for as many things there are in the list as many things it can sequence through ,and everytime it does, the variable i will always have a new value, i updates sequencially,the first time i run this loop i is the first item "foundations of decay", the second time i run this loop i is the second item it keeps going until it no longer has anything to sequence(pass through)through and there is no other thing for i to be,it's called i because it is referencing the index variable anything that has an index position in the thing we are sequencing through
# fav_songs = [
#     "The foundatioin of decay - my chemical romance", 
#     "Pandemonium - Killing Joke", 
#     "Jigsaw Falling into Place Radiohead",
#     "Army of me _ Dre"
# ]

# for i in fav_songs:
#     print("Thats a great song")
#for i in fav_songs:
#for i in range(0,10,1)
#     print(i)
# for i in range(2,10,2):
#     print(i)
#start/stop/step   
# for i in range(10, -1,-1):
#     print(i)    
#we don't have to reference the variable
#range function generates a sequnce of numbers for us to sequence through that's what we will iterate through
#from start to finish there would be 4 values 1 value for each item it sequences/passes through in the loop 
#it is called the i it is referencing the index variable anything that has an index position in the thing we are sequencing.
#for loop runs for as many things there are in the things we are looking in 
# favourite_drinks = ["coke", "fanta", "tonic"]
# for i in favourite_drinks:
#     print(i)
# for i in range(10):
#     print(i)
# for i in range(0, 10):
#     print(i)
# for i in range(2, 10, 2):
#     print(i)   
#range only needs one parameter/argument to work, the number 10 is the stop value because range is actually a 3 parameters, we only need to give it 1st parameter, that parameter we need to give it is the stop value because range is written in slice notation. the first nunmber you give it is the start value starting with a 0 and the second value is the stop at value 10 and this will always stop short the sequence before 10, 9,and the 3rd number is the step number which in this case it's just by adding 1 number each time. the only parameter that we need is that stop value and it's going go stop short. i moves within the ranks and each time changes it's value 
# for i in range(10, -1, -1):#10 is our start -1 stop (short) and -1 sequencing/stepping through that by minusing 1 each time taking 1 step back each time, range is used to give sequences to go through,  
#     print(i)
#the other kind of loop is the while loop
# num = 0

# while num != 10:
#     print(num)
#while a FOR LOOPS runs for a specific number of times for as many things it can sequence through, for as many things as there are in the things we are looking in,  it has a limit we can put a figure on how many times it will run, a WHILE LOOP on the other hand runs based on condition
# num = 0
# if num < 10:
#     num += this is a += operator sign, this adds 2 to what ever num is (to the value of num) and updates the value to have that and then runs once because it's an if statement,while on the other hand 
#     print(num)
    
num = 0
while num < 10:
    num += 1
    print(num)# this runs until num becomes 10 else the while loop is just going to keep adding one till is gets to 10 and then stops running