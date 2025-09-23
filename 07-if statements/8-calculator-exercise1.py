# python calc

num1 = float(input("Enter the 1st no: "))
operator = input("Enter operator (+ - * /): ")
num2 = float(input("Enter the 2nd no: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"'{operator}' is not a valid operator")