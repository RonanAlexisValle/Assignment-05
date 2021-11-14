#This will ask the user to input three random numbers
num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
num3 = float(input("Input the third number: "))

#This will show the smallest number on the console
if num1 < num2 and num1 < num3:
    print(num1,"is the smallest among three numbers.")
elif num2 < num1 and num2 < num3:
    print(num2,"is the smallest among three numbers.")
else:
    print(num3,"is the smallest among three numbers.")
    

