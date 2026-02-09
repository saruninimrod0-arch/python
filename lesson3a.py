# Boolen - This is date type that evaluates either to true or false

isRaining = False

print(isRaining)
print(type(isRaining))

paidloan = True
print(type(paidloan))

# comparison operators: Theu are used to compare two or more statments and they usually return a boolean answer

number1 = 2
number2 =5
print("is number greater than number 2?", number1 > number2)
print("is number less than number 2?", number1 > number2)
print("is number1 greater than or equal to number 2?", number1 >= number2)
print("is number1 greater than or equal to number 2?", number1 <= number2)
print("is number1 equal to number2?", number1 == number2)
print("is number1 equal to number2?", number1 != number2)

# Logical operators
# Logical AND
# It returns if an only if the condition/statements evaluates to true
print((3 > 1) and (7 > 6))
      
# Logic or 
# It evaluates to true if one of the statements/condition is true
print((3 > 1) or (7 < 6) or (10 > 5))

# Logic not
# It is used to negate a statement/condition
print(not(90 > 70))