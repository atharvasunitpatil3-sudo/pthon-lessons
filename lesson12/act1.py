# Write a program to check how many times a "letter" is repeated in a word
import time
while True:
    word = input("Enter a word : ").strip().lower()

    if word == "exit":
        print("Good Bye!....")
        break

    if not word.isalpha() or len(word) == 0:
        print("Invalid Input, The wor can only contain alphabetic letters..")
        continue

    letter = input(f"Enter a single letter to search in {word} : ")

    try:
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("You must enter only alphabetic letters")

    except ValueError as e:
        print(f"Error message : {e}")

    else:
        count_occurences = word.count(letter)
        if count_occurences > 0:
            print(f"Letter found {count_occurences} time(s)")
        else:
            print("not found...")

    for i in range(1, 6):
        time.sleep(1)  
        print(f"\rWaiting for next round..{i} sec", end='', flush=True)
    print()


