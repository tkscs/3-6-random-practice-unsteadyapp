# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = ["zebra","lion","dog"]
random.shuffle(animal)
animal = animal[0]
# Age (integer)
age = random.randint(1,100)
# Color (at least 3 choices, string)
color = random.choice(["zebra","lion","dog"])
# Weight (float)
weight = random.randint(5000,20000)/100
# Print a summary of your pet using an f-string
print(f"Your pet is a {animal} who is {age} years old")#REPLACE THIS WITH YOUR CODE