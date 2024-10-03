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
