def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "_":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

    print(calculator(10, 5, '+'))  # Output: 15
    print(calculator(10, 5, '-'))  # Output: 5
    print(calculator(10, 5, '*'))  # Output: 50
    print(calculator(10, 5, '/'))  # Output: 2.0