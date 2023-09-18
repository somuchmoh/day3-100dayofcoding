print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rollercoaster!") #This needs to be indented
else:
  print("Sorry, you have to grow taller before you can ride.")

#Nested ifs are if conditions inside another if condition 
if height > 120:
  print("You can ride the rollercoaster!") #This needs to be indented
  age = int(input("What is your age? "))
  if age < 12:
    print ("Please pay $5")
  elif age <= 18:             #If there are more than 2 conditions to test, then use elif (else, if)
    print ("Please pay $7")
  else:
    print ("Please pay $12")
else:
  print("Sorry, you have to grow taller before you can ride.")



#multiple if statements 
bill = 0

if height > 120:
  print("You can ride the rollercoaster!") #This needs to be indented
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print ("Please pay $5")
  elif age <= 18:      #If there are more than 2 conditions to test, then use elif (else, if)
    bill = 7
    print ("Please pay $7")
  else:
    bill = 12
    print ("Please pay $12")

  want_photo = input("Do you want a photo taken? Y or N. ")
  if want_photo == "Y":
    bill = bill + 3    #You can write it as bill += 3
    print (f"Please pay ${bill}.")
    
else:
  print("Sorry, you have to grow taller before you can ride.")


#Logical operators 
age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print ("Please pay $5")
  elif age <= 18:    
    bill = 7
    print ("Please pay $7")
  elif age > 44 and age < 56:         #This logical operator will only check if age is b/w 45 and 55
    bill = 0 
    print ("Your ticket is on us!")
  else:
    bill = 12
    print ("Please pay $12")
  
    