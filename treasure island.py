print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
cross_road1 = input("You are at a crossroads, do you want to go left or right? ")
cross_road = cross_road1.lower()

if cross_road == "right":
  print("Great! You've come across a river. What's next? ")
else:
  print("Oh no! You've fallen into a ditch :( Game Over!")


if cross_road == "right":
  river1 = input("Do you want to swim or wait? ")
  river = river1.lower()
  if river == "wait":
    print("Oh look, a boat! You've safely crossed the river and reached a mansion.")
  else:
   print("Oh no! You swam into crocodile infested waters :( Game Over!")


  if river == "wait":
    door1 = input("The mansion has 3 doors to enter. Which one do you choose? Red, Blue or Yellow? ")
    door = door1.lower()
    if door == "red":
      print("You've been caught by the beast :( Game Over!")

    if door == "blue":
      print("Looks like you've entered an empty room and you're trapped. Game Over!")

    if door == "yellow":
      print("You've found the treasure!")
