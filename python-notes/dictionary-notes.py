print("this is dictionaries")
#dictionaries store data for us in a really specific way, just like actual dictionaries you can look things up, but not in alphabetic order,they are more like lists they store multiple values to one variable we denote a dictionary by using curly brackets{}these are used to define our dictionaries,dictionary stores key:value pairs.Basically, they allow you to give each element a name, we will be using 2 bits of information the key and the value
#this is a dictionary, 3 items there in our dictionary made up of key:value,pairs, they all have key words and value. each key in the dictionary must be unique, they cannot have 2 named keys, it will just read whatever one it reads last if that's the case. no key duplicates are allowed,what duplicate values are allowed. we have a variable that's the name we are using to refer to all this data in the dictionary = signs are assignment operator as we are assigning them a dictionary to that variable then what makes it a dictionary is the curly braces and the key value pairs key and value = item.dictionaries do not have a numbered index, so we use different methods to extract or change values,dictionaries aren't indexed they don,t have a numbered index they have the key index print(my_dog[2])this means lookking for the key to which doesn't exist, so instead to find out information about our dictionaries we have to use different methods different ways to extract or change our values, very similar way in that the way we write it is the same we still put it in the square brackets it's still an object and a target, what we put in the brackets this time is the key we are looking for eg if i want to see the mood of my dog i would search for the key print(my_dog["mood"])instead, so rather than targetting that position numbers index, we target it through it's key insteadand this is why those keys have to be unique as well,because if i have 3 moods in there and set the program target mood which one , there is a parttern and similarity in the syntax what's in those square brackets isn't a number a not an index position number like we have been using previously, but in terms of target information it,s still syntaxically very similar, rather than using number because dictioinaries don't have, they are not indexed we use the key instead, so if i wanted to see my dog's name print(my_dog[name])
my_cat = {
    "name": "Salem",
    "colour": "Black",
    "mood": "Sassy"
}

my_dog = {
    "name": "Toby",
    "breed": "Keeshond",
    "mood": "Barky"
}
x=my_dog.keys()
my_dog["age"]=2
print(x)

print(my_dog.values())
print(my_dog.items())
print(my_dog.get("mood"))
print(my_dog.get("legs", "This key doesn't exist"))
# print(my_dog["Mood"])
# print(f'My dog {my_dog["name"]} is a bit {my_dog["Mood"]} today')

# print(my_dog.keys())
# my_list=["hello", "hello", "goodbye"]
# y = my_list.count("hello")
# my_list.append("hello")
print(my_dog["mood"])
print(my_dog["name"])