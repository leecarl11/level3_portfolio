test_string = "welcome to code nation"

string_len = len(test_string)

def odd_even_checker ():
    if string_len%2 == 0:
        print(f"the length of the string {test_string} is {string_len} and it is even")
    else:
        print(f"the length of the string {test_string} is {string_len} and it is odd")
        
odd_even_checker("hello")
odd_even_checker("hellos")
odd_even_checker("hellosss")
odd_even_checker("hey")