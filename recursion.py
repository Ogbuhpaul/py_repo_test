# Factorial in python


# def factorial(n):

#     if n <=1:
#         return n
#     else:
#         val = n + factorial(n-1)
#         print(val)
#         return val

# factorial(5)



# # COUNTDOWN WITH RECURSION
# def count_down(num):
#     if num == -1:
#         return num
#     print(num)
#     return count_down(num-1)

# count_down(50)






# # Recursive Python function to solve the tower of hanoi 

# def TowerOfHanoi(n , source, destination, auxiliary): 
# 	if n==1: 
# 		print ("Move disk 1 from source",source,"to destination",destination )
# 		return
# 	TowerOfHanoi(n-1, source, auxiliary, destination) 
# 	print ("Move disk",n,"from source",source,"to destination",destination )
# 	TowerOfHanoi(n-1, auxiliary, destination, source) 
		
# # Driver code 
# n = 3
# TowerOfHanoi(n,'A','B','C') 


# for loop solution of moving difference
previous_number = 0
numbers = [20, 60, 90, 103, 109, 120]

# for i in numbers:
#     print(i  - previous_number)
#     previous_number = i

# recursion solution of moving difference
def moving_difference(vals):
    
    if len(vals)==1:
        return 0

    else:
        previous_number = vals.pop(0)
        print(vals[0] - previous_number)
        return moving_difference(vals)

moving_difference(numbers)