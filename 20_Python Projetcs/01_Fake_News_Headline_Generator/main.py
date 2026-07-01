# 1. import random module
import random

# 2. create subjects
subjects = [
    "Sazim",
    "Virat Kohli",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "eats",
    "declares war on",
    "celebrates",
    "dance"
]

places =  [
     "in Puran Dhaka",
     "in Local Train",
     "in Ballfield",
     "at Sun Roof",
     "at Masud Kakar Dokan",
     "inside parliament"
]

# 3. start the headline generation
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another news? (yes/no)").strip().lower()
    if user_input == "no":
        break

# print goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day")