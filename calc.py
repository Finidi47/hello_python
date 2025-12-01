# A simple Calculator App

# Get first number
num1 = int(input("Enter your first number: "))

# Get second number
num2 = int(input("Enter your second number: "))

# Choose operator
operator = input("Choose operation (+, -, *, /, %): ")

# Compute the result
if operator == "+":
    ans = num1 + num2

elif operator == "-":
    ans = num1 - num2

elif operator == "*":
    ans = num1 * num2

elif operator == "%":
    if num2 == 0:
        ans = "Error!! Cannot divide by zero"
    else:
        ans = num1 % num2

elif operator == "/":
    if num2 == 0:
        ans = "Error!! Cannot divide by zero"
    else:
        ans = num1 / num2
else:
    ans = "invalid operation"


# Display the result
print(f"The answer is: {ans}")