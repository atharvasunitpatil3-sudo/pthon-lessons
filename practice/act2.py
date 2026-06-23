while True:
    # 1. Continously prompt the user for a word
    word = input("\nEnter a word( or type a 'exit' to quit): ").strip()

    #Optional: Add away to break the infinite loop
    if word.lower() == 'exit':
        print("Goodbye!")
        break

    # Skip if the user just pressed enter without typing a word
    if not word:
        print("You didn't enter anything. Try again.")
        continue
    # 2. Infinite loop for the letter unput and validation
    while True:
        letter = input("Enter a single letter to search for: ").strip()

        #Validate that the input is exactly one character
        if len(letter) != 1:
            print("wrong input , only one enter again")
            continue # Restarts the inner loop to ask tyhe letter again
        else:
            break # Valid input recieved, exit the validation loop

# 3. Check if the letter exists in the word and count occurrences
    if letter in word:
          count = word.count(letter)
          print(f"yes found. It appears {count} time(s).")  
    else:
          print(f"'{letter}' wass not found in '{word}'.")

    # The program will now automatically restart from the top and ask for a new word
      