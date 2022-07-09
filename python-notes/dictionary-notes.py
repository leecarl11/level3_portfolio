print("this is dictionaries")
#dictionaries store data for us in a really specific way, just like actual dictionaries you can look things up, but not in alphabetic order,they are more like lists they store multiple values to one variable we denote a dictionary by using curly brackets{}these are used to define our dictionaries,dictionary stores key:value pairs.Basically, they allow you to give each element a name, we will be using 2 bits of information the key and the value
#this is a dictionary, 3 items there in our dictionary made up of key:value,pairs, they all have key words and value. each key in the dictionary must be unique, they cannot have 2 named keys, it will just read whatever one it reads last if that's the case. no key duplicates are allowed,what duplicate values are allowed
my_cat = {
    "name": "Salem",
    "colour": "Black",
    "mood": "Sassy"
}

my_dog = {
    "name": "Toby",
    "breed": "Keeshond",
    "Mood": "Barky"
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