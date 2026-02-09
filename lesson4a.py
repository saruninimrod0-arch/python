# Nested if statements
# A nested if statements is an if statement that is contained within another if statements.

age = 20
weight = 60

if age > 15:
    if weight > 50:
        print("you can donate blood")
    else:
        print("you cannot donate blood because of weight")
else:
    print("you cannot donate blood because of your age")