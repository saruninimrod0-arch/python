# Python lists
# A lists python is a collection of items that ordered in a certain way.
# A lists is inroduced by use of the square brackets [].
# The items of a lists are stored inside of indexes. Note: programming we start counting from index Zero (0). bmw, benze, hiance, ...
# A lists is mutable  i.e the contents of a lists can be changed.

cars = ["BMW", "Benze", "Hiance", "Prado", "Probox", "Mclarel", "Range"]

print(cars)
print(type(cars))

# A ccessing items of a lists
print(cars[2])
print("The car on index four is", cars[4])

# List slicing - This is creating a list from a bigger list
print(cars[4:])

# printing from index zero index three
print(cars[:4])


# printing from hiance to probox
print(cars[2:5])

# Lists - Mutability
# we use the function append add an item at the end of a lists
cars.append("Marcedes")
print(cars)
cars.append("subaru")
print(cars)

# we use the pop function to remmove the list
cars.pop()
print(cars)

# we can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

# we can use sort function to sort our items in alphabetical order
cars.sort(reverse=True)
print(cars)