# Conditions in Python

# if-else statement

condition = ''

if condition:
    # code block to execute if condition is True
    print("The variable 'condition' is not empty.")
else:
    # code block to execute if condition is False
    print("The variable 'condition' is empty.")


 # Nested If Else Statement

gender  = input("Enter your gender (M/F): ")
age     = int(input("Enter your age: "))

if gender.upper() == 'M':
    print('Welcome Sir,')

else :
    if gender.upper() == 'F':   
        print('Welcome Madam,')
    else:
        print('Hello,')
        
        
        
if age >= 18 and age <= 40: 
    print('You are eligible for this job.')

else: 
    print('Sorry, You are not eligible for this job.')            