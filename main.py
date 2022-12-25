print("select operation")
print("1.ADD")
print("2.SUBTRACT")
print("3.DIVIDE")
print("4.MULTIPY")

operation = input()

if operation == "1":
    num1= input("enter first value: ")
    num2= input("enter second value: ")
    print("the answer is " + str(int(num1) + int(num2)))

if operation == "2":
    num1= input("enter first value: ")
    num2= input("enter second value: ")
    print("the answer is " + str(int(num1) - int(num2)))

if operation == "3":
    num1= input("enter first value: ")
    num2= input("enter second value: ")
    print("the answer is " + str(int(num1) / int(num2)))

if operation == "4":
    num1= input("enter first value: ")
    num2= input("enter second value: ")
    print("the answer is " + str(int(num1) * int(num2)))