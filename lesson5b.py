# Functions with a parameters
# They are values that get passed as arguments given to a function inside of the parenthesis.


def greeting(name):
    print(f"{name}How are you hope everything is fine.")

greeting("Bernard")
greeting("Nimrod")
greeting("Lenard")

print("===================================")
def message(names):
    print(f"Hello {names}. We shall be having a general on date....Please avail Yourself.")

message("Joy")
message("Stephene")

print("===================================")
# Create a parameter that accept parameters to add two numbers
def add_numbers (x,y):
    sum = x + y
    print(" The sum of the number is:", sum)
result = add_numbers(4,7)
print(result) 