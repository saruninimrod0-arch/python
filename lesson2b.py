# Tuple
# A tuple is a immutable type of a list (It cannot change)
# To use introduce a tupule, we use the parenthesis()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kjiado", "Kisii")

print(counties)
print(type(counties))

# slicing of tupules
print(counties[3:])

# accessing items of a tupule by use of indexes
print(counties[5])

# Note: Below will generate an error
counties.append("Machakos")
print(counties)