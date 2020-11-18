# faulty calculator
"""design a calculator which will correctly solve all the problems except the following ones
45*3=555,56+9=77,56/6=4
your program should take opreator and the two numbers as input from user
and then return the result"""
print("Enter the opreator ")


op=input()
print("Enter two numbers")
num1 = input()
num2 = input()

if op == "+":
    if num1 == int(56) and num2 == int(9):
        print(int(77))
    else:
        print(int(num1) + int(num2))

elif op == "*":
    if num1 == 45 and num2 == 3:
        print(555)
    else:
        print(int(num1)*int(num2))

elif op == "-":
    print(int(num1)-int(num2))

elif op == "/":
    if num1 == 56 and num2 == 6:
        print(4)
    else:
        print(int(num1)/int(num2))
# not completed