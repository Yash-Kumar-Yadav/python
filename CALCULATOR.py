print('''
* MULTIPLY
/ DIVIDE
''')
num1=int(input("Enter the value:-"))
num2=int(input("Enter the value:-"))
opr=input("Enter the operator..(+,-,*,/):- ")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid operator")
