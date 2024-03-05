num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
start = min(num1, num2)
end = max(num1, num2)
for i in range(start, end + 1):
    if i % 5 == 0:
        print(i)