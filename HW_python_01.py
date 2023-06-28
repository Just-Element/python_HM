print("Welcome to the Calculator Program!")

try:
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    print('''Please select an operation: 
    1. Addition 
        2. Subtraction 
            3. Multiplication 
                4. Division''')
    
    operation = int(input("Enter your choice (1-4): "))

except ValueError:
    print("Pleas try again")

else:
    if operation == 1:
            Addition = int(num1 + num2)
            print(f'The result of multiplication is: {Addition}')
    elif operation == 2:
            Addition = int(num1 - num2)
            print(f'The result of multiplication is: {Addition}')
    elif operation == 3:
            Addition = int(num1 * num2)
            print(f'The result of multiplication is: {Addition}')
    elif operation == 4: 
        try:
            Addition = int(num1 / num2)
            print(f'The result of multiplication is: {Addition}')
        except ZeroDivisionError:
            print("Division by 0 is not available")

            
            
