# Task 1: Identify the greatest number
# Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Identify the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print out the largest number
print("The largest number is:", largest)

#Task 2: Identify the smallest number

# Identify the smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Print out the smallest numbers
print("The smallest number is:", smallest)

# Task 3: Equal number
# Check if all numbers are equal
if num1 == num2 == num3:
    print("All numbers are equal.")
else:
    # Identify the largest number
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    
    # Check if two numbers are equal
    if num1 == num2 and num2 == num3:
        print("All numbers are equal.")
    elif num1 == num2:
        print("The first and second numbers are equal.")
    elif num1 == num3:
        print("The first and third numbers are equal.")
    elif num2 == num3:
        print("The second and third numbers are equal.")
    else:
        print("The numbers are all different.")
    
    # Identify the smallest number
    if num1 <= num2 and num1 <= num3:
        smallest = num1
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
    else:
        smallest = num3

