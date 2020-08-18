# def say_hello(name):


#     """"THIS FUNCTION IS JUST ABSOLUTELY HUMBLE.. AND THIS IS A DOCSTRING!!!""""


#     print(f"Hello {name}.")

#     say_hello("Bolu..!!")

# def sqrt(number,power):
#         answer = number**(1/power)
#         # print(answer)
        # return answer
# x = sqrt(9,2)
# print (x)

# y = (sqrt(9,2) * sqrt(4,2))
# print(y)



# def sqrt(number1,number2,power):
#     y = (number1**(power) + number2**(power))**(1/power)
#     return (y)
# y = sqrt(3,4,2)
# print (y)




# import datetime

# time_now = datetime.datetime.now()
# print(time_now.weekday()) # Gives week day in numerals

# print(time_now.strftime("%a %H:%M.")) #Gives a formatted string representation of the time

# time_stamp = time_now.strftime("%a %H:%M.")
# file = open("text_files/notes.txt", "w")

# text = input("Enter Text: ")

# file.write(text)








# import datetime
# def get_timestamp():

#     time_now = datetime.datetime.now()
#     time_stamp = time_now.strftime("%a %b %H %M.")
#     print(time_stamp)
#     return time_stamp

# def store_memory(memory,time_stamp,txt_len):
#     file = open(f"text_files/{time_stamp}--{txt_len}.txt","w")
#     file.write(memory)
#     file.close()

#     return True



# def get_text_len(text):
#     return len(text)



# text = input("Please Enter Text: ")
# time_stamp = get_timestamp()
# store_memory(text, time_stamp, get_text_len(text))
# # print(len(text))





# functions with variable positional arguments
def sum_nums(*args):
    print(args)
sum_nums(3,2,4,5,6,7,8,8,8,8,8,88,4,3324,688)

#Functions with keyword arguments
def sum_nums(**kwargs):
    print(kwargs)

sum_nums(x=2, y=3, z=4, q=6)