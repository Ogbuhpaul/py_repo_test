# for i in "banana":
#     print (i)
#     print("")

# while True:
#     print ("I am running!!")
#     print(".......!") 







# word = "Program"
# index = 0



# while True:
#     index += 1
#     print (index)

#     if index == 6:
#         break



# word "Emancipation

# for letter in word":
#     print


# sentence = "In this example, <iterable> is the list a and <var> is the variable i. "

# word_list = sentence.split(" ")
# # print(word_list)
# place_holder = " "

# for word in word_list:

#     if len(word) > len(place_holder):
#         place_holder = word
# print (place_holder)


# step_value = 2
# number =0
# stop_value =200


# while True:
#     print(number)
#     number +=1

#     if number == stop_value:
#         break




# import time
# import winsound

# number_of_seconds = int(input("Enter time in seconds: "))

# for i in reversed(range(number_of_seconds)):
#     print(i)
#     time.sleep(1)
# winsound.Beep(500,1000)









# Write a script factors.py that asks the user to input a positive integer
# and then prints out the factors of that number. Here’s a sample run
# of the program with output




# for i in range(100,999):

#     sum_nums = i * 3
#     last_nums = str(i)[2] * 3

#     if sum_nums == int(last_nums):
#         print(i, sum_nums,last_nums)
#         break





# numbers =[50 ,10, 100, 99, 80, 80, 30]
# numbers_deviation = []
# numbers_deviation_squared = []

# n = len(numbers)
# mean = sum(numbers)/n

# for number in numbers :

#     print(number - mean)


# for number in numbers:
#     numbers_deviation.append(number - mean)
#     print(number - mean)

# print(numbers_deviation)


# for number in numbers:
#     numbers_deviation_squared.append(number - mean)
#     print(number)





# file_name = "text_files/buhari.txt"
# file = open (file_name,"r", errors= "ignore")
# data = file.read()
# print (data)

# word_list = data.split(" ")
# buhari_place_holder = " "

# for word in word_list:

#     if len(word) > len(place_holder):
#         place_holder = word

# print (place_holder)


# file_name = "text_files/obama.txt"
# file = open (file_name,"r", errors= "ignore")
# data = file.read()
# print (data)

# word_list = data.split(" ")
# obama_place_holder = " "

# for word in word_list:

#     if len(word) > len(place_holder):
#         place_holder = word

# print (place_holder)

# longestword_owner = "Buhari" if len(buhari_placeholder) > len(obama_place_holder) else "obama"
# print(longest_owner)






# file_name ="text_files/num_file.csv"
# file = open(file_name, "w")

# numbers = [50,10,100,90,80,30]

# file.write(f"Scores, Passed\n")
# for number in numbers:
#     file.write(f"{number}, {number >50} \n")


file_name ="text_files/num_file.csv"
file = open(file_name, "w")

numbers = [-14.4, -54.4, -35.86, -34.86, -15.86, -15.86, -34.14]

n = len(numbers)
mean = sum(numbers)/n

file.write(f"Scores, x-xbar\n")
for number in numbers:

    file.write(f"{number}, {number-mean}\n")