import random
CompNumber=random.randrange(1,201)
userInput=int(input("Input from user:-"))
if userInput>CompNumber:
    print("Computer Number is  ",CompNumber)
    print("Your value is high")
elif userInput<CompNumber:
    print("Computer Number is  ",CompNumber)
    print("Your value is low")
else:
    userInput=CompNumber
    print("Computer Number is  ",CompNumber)
    print("Your value is correct")
