# Operators: Arithmetic ( +, -, /, *, //, **, % )

# Arthematic  operators are used to perform basic mathematical operations. 

# Addition (+) : It is an operator that adds two numbers together and returns the result. 
num1 = 5
num2 = 3
sum = num1 + num2   # The "+" operator can be used for addition.
print(f"The sum of {num1} and {num2} is {sum}")  # Output: The sum of 5 and 3 is 8

# Subtraction (-): This operator subtracts the second number from the first number and returns the result.
diff = num1 - num2     # "-" operator can also be used for subtraction.
print(f"The difference between {num1} and {num2} is {diff}")  # Output: The difference between 5

# Division  (/): This operator divides the first number by the second number and returns the quotient.
quotient = num1/num2       # "/" operator is used for division.
remainder = num1%num2        # "%" operator gives the remainder after division
print(f"{num1} divided by {num2} is {quotient} with a remainder of {remainder}")   # Output: 5 divided by 3 is 1.6 and its reminder is 2.

# (//)  Floor Division: This operator performs floor division where the decimal part is removed and only the integer part
quotient2 = num1//num2    
print(f"\nQuotient when {num1} divided by {num2} is {quotient2}") # Output: Quotient when 5 divided by 3 1

# (**)  Power operator: Raises the base number to the power of the exponent.
power = num1**num2         # "**" operator is used for raising a number to another number.
print(f"\n{num1} raised to the power of {num2} is {power}")    # Output: 5 raised to the power of 3 is 125
