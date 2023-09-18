# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
div_4 = year % 4 
div_100 = year % 100
div_400 = year % 400

if div_4 == 0:
    if div_100 == 0:
        if div_400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    if div_100 != 0:
        print ("Leap year.")
else:
    print ("Not leap year.")