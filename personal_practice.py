
# num = input("Enter a number to be doubled: ")
# doubled_num = float(num) * 2
# print(doubled_num)


# num1 = input("Please Enter First Number: ")
# num2 = input("Please Enter Second Number: ")
# result = int(num1) * int(num2)
# print(f"The product of {num1} and {num2} is {result}")


# name = "Zaphod"
# heads = 2
# arms = 3

# # # print(f"{name} has {heads} heads and {arms} arms")

# # # print(name "has" str(heads) "heads and" +str
# print(name, "has", str(heads), "heads and", str(arms), "arms")



# weight = 0.2
# animal = "newt"
# # print(f"{weight} is the weight of the {animal}")

# # print("{} is the weight of the {}".format(weight,animal))

# print (str(weight) + " is " + "the weight of the "+ (animal))




# Challenge
# Write a script called translate.py that asks the user for some input
# with the following prompt: Enter some text:. Then use the .replace()
# method to convert the text entered by the user into “leetspeak” by making
# the following changes to lower-case letters

# leet = ("Enter some text: ")




# def greet(name):
#     print(f"Hello, {name}!")
# greet("dave")



# def multiply(x, y):
#     product = x * y
#     return product

# num = multiply(2,4)
# print(num)






# Write a function called cube() with one number parameter and returns
# the value of that number raised to the third power. Test the
# function by displaying the result of calling your cube() function on
# a few different numbers.

# def cube(x):
#     triple = x * x * x
#     return triple

# num = cube(50)
# print(num)



# def greet(name):
#     print(f"Hello, {name}!")
# greet("dave")











# #importing the time module
# import time

# #welcoming the user
# name = raw_input("What is your name? ")

# print "Hello, " + name, "Time to play hangman!"

# print "
# "

# #wait for 1 second
# time.sleep(1)

# print "Start guessing..."
# time.sleep(0.5)

# #here we set the secret
# word = "secret"

# #creates an variable with an empty value
# guesses = ''

# #determine the number of turns
# turns = 10

# # Create a while loop

# #check if the turns are more than zero
# while turns > 0:         

#     # make a counter that starts with zero
#     failed = 0             

#     # for every character in secret_word    
#     for char in word:      

#     # see if the character is in the players guess
#         if char in guesses:    
    
#         # print then out the character
#             print char,    

#         else:
    
#         # if not found, print a dash
#             print "_",     
       
#         # and increase the failed counter with one
#             failed += 1    

#     # if failed is equal to zero

#     # print You Won
#     if failed == 0:        
#         print "
# You won"  

#     # exit the script
#         break              

#     print

#     # ask the user go guess a character
#     guess = raw_input("guess a character:") 

#     # set the players guess to guesses
#     guesses += guess                    

#     # if the guess is not found in the secret word
#     if guess not in word:  
 
#      # turns counter decreases with 1 (now 9)
#         turns -= 1        
 
#     # print wrong
#         print "Wrong
# "    
 
#     # how many turns are left
#         print "You have", + turns, 'more guesses' 
 
#     # if the turns are equal to zero
#         if turns == 0:           
    
#         # print "You Lose"
#             print "You Lose
# "  




# convert_cel_to_far() which takes one float parameter representing
# degrees Celsius and returns a float representing the same temperature
# in degrees Fahrenheit using the following formula:
# F = C * 9/5 + 32





# def convert_cel_to_far(deg_cel):
#     """Returns the converted equivalent of the number"""
#     Far = deg_cel * 9/5 + 32
#     return Far

# converted = convert_cel_to_far(56.0)
# print(converted)





# convert_far_to_cel() which take one float parameter representing
# degrees Fahrenheit and returns a float representing the same temperature
# in degrees Celsius using the following formula:
# C = (F - 32) * 5/9


# def convert_far_to_cel(deg_far):
#     Cel = (deg_far - 32) * 5/9
#     return Cel

# converted = convert_far_to_cel(400.0)
# print(converted)




# cel_convert = input("Enter a temperature in degrees F: ")
# def convert_far_to_cel(cel_convert):
#     Result = (cel_convert - 32) * 5/9
#     return Result
# converted = convert_far_to_cel(float(cel_convert))
# print(f"{cel_convert}degrees F = {converted:.2f} degrees C")










# cel_convert = input("Enter a temperature in degrees C:")
# def convert_cel_to_far(cel_convert):