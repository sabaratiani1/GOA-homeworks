def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Check if the first character of a string is 'G'
def starts_with_G(s):
    if s[0] == 'G':
        return True
    else:
        return False

# Program to check if a number is even and print the next even number
def check_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is not even.")
        print("Next even number:", num + 1)

# While loop to ask for password until correct
incorrect_count = 0
while True:
    password = input("Enter the password: ")
    if password == "Goa best":
        print("Correct password entered.")
        break
    else:
        incorrect_count += 1

print("Incorrect password attempts:", incorrect_count)

# Ask for five names and print the first three
names = []
for _ in range(5):
    name = input("Enter a name: ")
    names.append(name)
print("First three names:", names[:3])

# While loop to print numbers from 10 to 0
num = 10
while num >= 0:
    print(num, end=' ')
    num -= 1
print()

# Simple calculator implementation
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, **): ")
num2 = float(input("Enter second number: "))

result = None
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero.")
elif operator == '**':
    result = num1 ** num2

if result is not None:
    print("Result:", result)
else:
    print("Invalid operator.")

# Ask user for name and print the last character
name = input("Enter a name: ")
print("Last character of the name:", name[-1])

# Using for loop, ask user for number and create a list of even numbers
user_num = int(input("Enter a number: "))
even_numbers = []
for num in range(user_num + 1):
    if num % 2 == 0:
        even_numbers.append(num)
print("List of even numbers up to", user_num, ":", even_numbers)

# Ask user for a whole number and calculate its factorial
user_number = int(input("Enter a whole number: "))
print("Factorial of", user_number, ":", factorial(user_number))