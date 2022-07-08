#CONVERTING DATA TYPES

#METHODS are things we do to our data
#PROPERTIES are things about our data 

#are all methods, these are built in functions that convert one data type to another
from xml.sax.handler import property_interning_dict


int()#this converts to integer data type
float()#this converts to floating point data type
str()#this converts to string data type
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

balance = 100
deposit = float(input("How much do you want to deposit? "))
balance +=deposit

print(f"You have {balance}")