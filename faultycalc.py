#2 - Faulty Calculator
# 45*3 = 555, 56+9 = 77 , 56/6 = 4
# Design a caluclator which will correctly solve all the problems except
# the following ones:
# Your program should take operator and the two numbers as input from the user and then return the result

num1 = int(input("Enter your First Number:\n"))
print("1.Add-->+\n2.Substract-->-\n3.Multiply-->*\n4.Divide-->/")
op = input("Enter your operator:--->")
num2 = int(input("Enter your Second Number:\n"))


if num1 == 45 and num2 == 3:
    if op == "*":
        print("Your Answer is 555")
elif num1 == 56 and num2 == 9:
    if op =="+":
        print("Your Answer is 77")
elif num1 == 56 and num2 == 6:
    if op == "/":
        print("Your Answer is 4")

elif op == "+":
    print("Answer is " ,num1+num2)
elif op == "-":
    print("Answer is " ,num1-num2)
elif op == "*":
    print("Answer is " ,num1*num2)
elif op == "/":
    print("Answer is " ,num1/num2)
else:
    print("Invalid operator")