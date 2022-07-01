def is_answer_num():
    answer = input("please type in a number ")
    #error handling
    try:
        print(int(answer))
        print(type(int(answer)))
    except:
        print("try again")
        is_answer_num()
        
is_answer_num()