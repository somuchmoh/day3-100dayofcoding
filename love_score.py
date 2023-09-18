# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_name1 = name1.lower()
new_name2 = name2.lower()

new_count1 = new_name1.count("t") + new_name1.count("r") + new_name1.count("u") + new_name1.count("e")

new_count2 = new_name2.count("t") + new_name2.count("r") + new_name2.count("u") + new_name2.count("e")

new_count3 = new_name1.count("l") + new_name1.count("o") + new_name1.count("v") + new_name1.count("e")

new_count4 = new_name2.count("l") + new_name2.count("o") + new_name2.count("v") + new_name2.count("e")

love_score1 = new_count1 + new_count2
love_score2 = new_count3 + new_count4

total_love_score = 10*(love_score1) + love_score2

if total_love_score < 10 or total_love_score > 90:
    print (f"Your score is {total_love_score}, you go together like coke and mentos.")
elif total_love_score > 40 and total_love_score < 50:
    print (f"Your score is {total_love_score}, you are alright together.")
else:
    print (f"Your score is {total_love_score}.")

