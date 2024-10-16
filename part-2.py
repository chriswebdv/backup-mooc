#fix syntax
# Fix the program
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now", number)
print(number, " must be my lucky number!")
print("Have a nice day!")

#Find the number of characters in a string and return only the one greater than 1 character length
# Write your solution here
char = input("Please type in a word: ")
if len(char) > 1:
    print(f"There are {len(char)} letters in the word {char}")
print("Thank you!")

#use typecasting function to get the decimal part of a floating number
# Write your solution here
num = float(input("Please type in a number: "))
print(f"Integer part:{int(num)}")
print(f"Decimal part: {num - int(num)}")

#write and function with check the age of the user

# Write your solution here

age = int(input("What is your age? "))

if age < 5 and age >= 0:
    print("I suspect you can't write quite yet...")
elif age < 0:
    print("That must be a mistake")
else:
    print(f"Ok, you're {age} years old")

# use or combined with an if statement to find the correct name of a nephew
# Write your solution here
#Huey, Dewey or Louie
name = input("Please type in your name: ")

if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# first while loop tp test if it works
# Write your solution here
while True:
    print("hi")
    str = input("Shall we continue? ")
    if str == "no":
        break
print("okay then")
