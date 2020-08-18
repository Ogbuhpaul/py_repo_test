# q = [1,2,3,4,5,6,7,8,9,10]

# y = q[-1]
# print (y)







# Student_scores = [
#     ["atha", [
#             ["m", 30],
#             ["e", 30]
#         ],
#         ["Hobbies",[
#             ["Running", "20%"],
#             ["Singing", "80%"]
#         ]]
#     ],
#     ["bolu",[
#             ["m", 30],
#             ["e", 30]
#         ],
#         ["Hobbies",[
#             ["Playing guitar", "80%"],
#             ["Pressing laptop", "20%"]
#         ]
#         ]
#     ],
#     ["Seun", [
#             ["m", 30],
#             ["e",30]
#         ],
#         ["Hobbies",[
#             ["Reading", "40%"],
#             ["Talking", "60%"]
#         ]
#     ]
#     ]
#     ]
    

    
    
# atha_name = Student_scores[0][2][1][1][1]
# print(atha_name)
# # # atha_score = Student_scores[0][1][0]
# # print(atha_score)
# bolus_hobby = Student_scores[2][2]
# print(bolus_hobby)



# for target_student in Student_scores:
#     name = target_student[0]
#     print('Name: ", name')


#     math_score = target_student[1][0][1]
#     print("Math Score : ", math_score)

#     english_score = target_student[1][0][1]
#     print("English Score : ", english_score)

#     hobbies =target_student[2]

#     hobby1_is_greater = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1])
#     favourite_hobby = hobbies[0][0] if hobby1_is_greater == True else hobbies[1][0]
#     print("Favourite Hobby is: ",favourite_hobby)



#     print()
#     print("--------------------------")
#     print("--------------------------")
#     print()




# While Loop Solution Of List Tuple
# names = ["John", "paul","Sean"]

# index = 0

# while True:

#     # print(index, names[index])

#     names[index] = "Mr" + names[index]

#     index += 1

#     if index == len(names):
#         break

# print(names)


# For Loop Solution Of List Tuple


# names = ["John", "paul","Sean"]

# for index in range(len(names)):
#     names[index] = "Mr" + names[index]

# print(names)





# a = []
# item_cart =input("Please Enter an item")
# a.append(a)


# Second Classwork
# list_of_values_entered =[]
# while True:

#     value = input("Please enter a value \n:")
#     list_of_values_entered.append(value)

#     for value in list_of_values_entered:
#         print(value.center(10), str(len(value)).center(10), len(value).center(10))
          



# list_of_values_entered = []
# while True:
#     value = input("Please Enter a Value: ")
#     list_of_values_entered.append(value)
#     print("You Now Have",len(list_of_values_entered),"Values in your list")

#     stop_or_continue = input("press y to continue entering values or n to stop \n:")

#     if stop_or_continue == "n":
#         break

# total_characters = 0
# print("value".center(10),"length".center(10),"quantity_of_A".center(16), "quantity_of_B".center(16), "quantity_of_C".center(16))
# for value in list_of_values_entered:
#     length_of_value = len(value)
#     total_characters += length_of_value
#     quantity_of_A = value.count("a")
#     quantity_of_B = value.count("b")
#     quantity_of_C = value.count("c")
#     print(value.center(10), str(length_of_value).center(10), str(quantity_of_A).center(16), str(quantity_of_B).center(16), str(quantity_of_C).center(16))
# print(f"\n Values in list:{len(list_of_values_entered)}, Total characters : {total_characters}, Quantity A: {quantity_of_A},Quantity B:{quantity_of_B},Quantity C: {quantity_of_C}")

# count = value.count('a')
# count = value.count('b')
# count = value.count('c')


# name = "Ezekiel"
# figure = 34
# print (name + " "+str(figure))




word = list("alphabet")
numbers = list("12345678")

# zipped_vals = zip(word, numbers)
# # print(next(zipped_vals))
# print(list(zipped_vals))


# def mini (x):
#     return "A" + str(x)

# mapped_result = map(mini,numbers)
# print(mapped_result)
# print(list(mapped_result))


mini2 = lambda x: "A"+ str(x)
# mapped_result = map(mini, numbers)
# print(list(mapped_result))

mapped_result2 = map(mini2, numbers)
print(list(mapped_result2))