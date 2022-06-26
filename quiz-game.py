# Welcome user
print("Welcome to Test Your Knowledge!")

# User enters their name and must answer yes to continue otherwise application exits.
name = input("Please enter your first name: ").capitalize()
playing = input(f"Welcome {name}! Do you want to play Test Your Knowledge? ")

if playing.lower() != "yes":
    exit()

print("Okay! Let's play =)")
# Score variable that will increment with correct answers.
score = 0

# Question 1
answer = input("What does HTML stand for? ")
if answer.lower() == ("hypertext markup language"):
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 2
answer = input("What does CSS stand for? ")
if answer.lower() == ("cascading style sheets"):
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 3
answer = input("What does JS stand for? ")
if answer.lower() == ("javascript"):
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 4
answer = input("What does SQL stand for? ")
if answer.lower() == ("structured query language"):
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 5
answer = input("What does OOP stand for? ")
if answer.lower() == ("object oriented programming"):
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Number of questions correct and score percentage for user
print(f"You got {score} questions correct.")
print(f"Your final score was " + str((score / 5) * 100) + "%.")