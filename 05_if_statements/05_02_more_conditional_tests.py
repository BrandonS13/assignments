#this code shows the difference between "==" and "!=".
#instead of using 2 different variables, I used the same variable and just changed the capitalization to show that it wouldn't reconize it
#I also ran tests using ">", "<", ">=", "<=" to show how they work with numbers
#I also perposefully added a false statement to each test so that I can understand how it reads the options
#I used and and or to show how 2 compomemts can be used to make a statement true or false

  
car = "jeep"
print(car == "jeep")
print(car != "bronco")
name = "Brandon"
print(name == "brandon")
print(name.lower() == "brandon")
age = 18
print(age == 17)
print(age != 20)
print(age > 16)
print(age < 21)
print(age >= 18)
print(age <= 18)
age = 18
grade = 12
print(age == 18 and grade == 12)
print(age == 18 and grade == 11)
print(age == 18 or grade == 11)
print(age == 17 or grade == 11)
sports = ["soccer", "basketball", "baseball"]
print("soccer" in sports)
print("football" in sports)
print("football" not in sports)
print("soccer" not in sports)