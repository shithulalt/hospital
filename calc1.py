# 2 - Faulty Calculator using functions
# Design a calculator which will correctly solve all the problems except
# the following ones: 45*3 = 555, 56+9 = 77 , 56/6 = 4
def calc(num1,num2,op):
    if num1 == 45 and num2 == 3:
        if op == "*":
            print("Your Answer is 555")
    elif num1 == 56 and num2 == 9:
        if op == "+":
            print("Your Answer is 77")
    elif num1 == 56 and num2 == 6:
        if op == "/":
            print("Your Answer is 4")

    elif op == "+":
        print("Answer is -->", num1 + num2)
    elif op == "-":
        print("Answer is -->", num1 - num2)
    elif op == "*":
        print("Answer is -->", num1 * num2)
    elif op == "/":
        print("Answer is -->", num1 / num2)
    else:
        print("Invalid operator")
result='y'
while(result=='y'):
    num1 = int(input("Enter your First Number:\n"))
    print("Add-->+\nSubstract-->-\nMultiply-->*\nDivide-->/")
    op = input("Enter your operator:--->")
    num2 = int(input("Enter your Second Number:\n"))
    calc(num1,num2,op)
    result = input("if you want to continue press 'y' else press 'n'\n")


