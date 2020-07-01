# put your python code here
num1 = float(input())
num2 = float(input())
operator = input()

if num2 == 0 and operator in ("/", "mod", "div"):
    print("Division by 0!")
else:
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "mod":
        print(num1 % num2)
    elif operator == "pow":
        print(num1 ** num2)
    elif operator == "div":
        print(num1 // num2)
