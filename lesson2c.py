# A dictionary is a data type that stores data in terms of key- value pair.
# It is introduced by the use of curly braces{}
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary we use the keys


phonebook ={
    "Saruni" : "254725511724",
    "Moses" : "2542265443987",
    "Kiyapi" : "254876543909"
  }

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# print out saruni's number
print(phonebook["Saruni"])

print('=======================')

player ={
    "name" : "Messi" ,
    "age" : 40,
    "teams" : ["PSG", "Barcelone", "Argentina"],
    "More" : {
        "Children" : 3,
        "Residents" : "US",
    "Phone" : (25477455434, 2547686697, 254678998)

 }
}
# print barcelona - the second team he played for
print(player["teams"][1])

