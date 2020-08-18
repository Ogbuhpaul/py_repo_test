# text = "Hello {Mr} {Adams}, we realized that you recently signed up for our weight loss program, we see that you are a {130kgs} and 5ft tall which gives you a BMI of {23}and by standards is {good}, hence we recommend the {sustainance} package for you today. buy now at {200}naira"


gender = input ("Please Enter gender,Mr/Mrs: ")
weight = input("Please Enter Weight: ")
height = input("Please Enter Height: ")

weight = int(weight)
height = int(height)
BMI = (weight / (height *height))
BMI = int(BMI)

text = f'Hello {"Mr" if gender == "Male" else "Mrs"} Adams, we realized that you recently signed up for our weight loss program, we see that you are {weight}Kg/s and {height}Ft tall which gives you a BMI of {BMI}Kg/m2 and by standards is {"good" if BMI >=25 else "You are FAT!!"}, hence we recommend the {"sustainance" if BMI >=25 else "weight loss"} package for you today. buy now at {"200"}naira'

print (text)
