myNumber1 = int(input("Enter your value 1:- "))
myNumber2 = int(input("Enter your value 2:- "))
enterOpr = input("Enter the operator +, -, *, /, % = ")
if enterOpr == "+":
    print(myNumber1 + myNumber2)
elif enterOpr == "-":
    print(myNumber1 - myNumber2)
elif enterOpr == "*":
    print(myNumber1 * myNumber2)
elif enterOpr == "/":
    print(myNumber1 / myNumber2)
elif enterOpr == "%":
    print(myNumber1 % myNumber2)
else:
    print("Invalid Operator")
