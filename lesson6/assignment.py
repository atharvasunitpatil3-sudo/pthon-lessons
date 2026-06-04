# Ask the user for a word and a letter
word = input("Enter a word :")
letter = input("Enter a letter:")

#Check if exactly one letter was entered
if len(letter) != 1:
    print("Invalid input! Please enter only one letter.")
else:

#Check if the letter is present in the word 
if letter in word:
    print("Letter found!")
else:
    print("Letter not found!")