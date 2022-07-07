# int(5.4)
# int("54")

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
fav_songs = ["the foundations of decay - my chemical romance", "Pandemonium - killing joke", "jigsaw falling into place radiohead", "army of me _Bkorks"]
#start:stop:step
print(fav_songs[1])#this is index position - it is the start value
print(fav_songs[1:2:1])#this is actually whats happening -starting short of 2,and stepping by 1 at a time
