#Here are the Python solutions for the five assignment tasks in the image:
#1: Function Without Parameters
def area_of_rectangle():
    length = 10
    width = 5
    area = length * width
    print(area)
    area()# involving the function
    print("===================================")

    
#2: Function With Parameters
def arithmetic_operations(a, b):
    sum_ = a + b
    difference = a - b
    product = a * b
    division = a / b if b != 0 else "Undefined (division by zero)"
    return sum_, difference, product, division

result=arithmetic_operations(10,6)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Division:", result[3])

print("===================================")


#3: Control Statement (if...elif...else)
def check_number():
    num = float(input("Enter a number: "))
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

print("===================================")
#4: Loop with Arithmetic
def sum_of_numbers():
    n = int(input("Enter a number n: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("The sum of numbers from 1 to", n, "is:", total)

print("===================================")
#5: While Loop
def square_of_numbers():
    n = int(input("Enter a number n: "))
    i = 1
    while i <= n:
        print("Square of", i, "is:", i ** 2)
        i + -1
        print(input("Enter a number: "))
        square_of_numbers(n)