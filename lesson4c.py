# A for loop can also used iterate through a list, tuple, string or even adictionary--

name = "Nimrod"

for letter in name:
    if letter == "n":
     print("the letter is n")
else:
    print(letter)

    print("===================================")
    # Below is a lists of counties
    counties = ["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Machakos", "Meru", "Nakuru", "Embu"]
    print(counties)

    for county in counties:
     print(county)
    
    print("===================================")
for "Nakuru" in counties:
   print("The county is part of the list of counties")
   break
else:
   print("The county is most part of the of the lists")


   print("===================================")

   player ={
      "name": "Mbappe",
      "age": 25,
      "teams": ["PSG", "Monaco", "France"],
      "nationality": "French"
      
   }
   for key in player:
      print(key)

   print("===================================")

   for value in player:
    print(player[value])
   # print(player["name"])



   print("===================================")
   # loop through the teams the player has played for
   # print(player[teams])


   for teams in player:["teams"]
   print(teams)