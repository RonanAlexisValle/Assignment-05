#This will ask the user to input the grade percentage
def InputGrade():
    InputGrade = float(input("Input grade percentage: "))
    return InputGrade

#This is the grade equivalent of the inputted grade
def gradeEquivalent():
    if userInput >=97 and userInput <=100:
        print("Your grade/mark is 1.0\nDescription: Excellent!")

    elif userInput >=94 and userInput <=96:
        print("Your grade/mark is 1.25\nDescription: Excellent!")

    elif userInput >=91 and userInput <=93:
        print("Your grade/mark is 1.5\nDescription: Very Good!")

    elif userInput >=88 and userInput <=90:
        print("Your grade/mark is 1.75\nDescription: Very Good!")

    elif userInput >=85 and userInput <=87:
        print("Your grade/mark is 2.0\nDescription: Good!")

    elif userInput >=82 and userInput <=84:
        print("Your grade/mark is 2.25\nDescription: Good!")

    elif userInput >=79 and userInput <=81:
        print("Your grade/mark is 2.50\nDescription: Satisfactory")

    elif userInput >=76.0 and userInput <=78:
        print("Your grade/mark is 2.75\nDescription: Satisfactory")

    elif userInput ==75:
        print("Your grade/mark is 3.0\nDescription: Passing")

    elif userInput >=65 and userInput <=74:
        print("Your grade/mark is 5.0\nDescription: Failure")

    else:
        pass

userInput = InputGrade()
userInput = round(userInput)
gradeEquivalent()