def calculate(expression):
    """
    Function to calculate the result of a mathematical expression.
    Supports addition, subtraction, multiplication, and division.
    """
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}

    # Initialize variables
    current_number = ''
    numbers = []
    ops = []

    # Iterate through the expression
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        elif char in operators:
            numbers.append(float(current_number))
            ops.append(char)
            current_number = ''
    
    # Add the last number to the list
    numbers.append(float(current_number))
    
    # Initialize result with the first number
    result = numbers[0]

    # Perform calculations based on operators
    for i in range(1, len(numbers)):
        result = operators[ops[i - 1]](result, numbers[i])

    return result

# Example usage:
expression = input("Enter a mathematical expression without spaces (e.g., 2+3*4/2): ")
result = calculate(expression)
print("Result:", result)
