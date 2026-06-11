total_numbers = 40
incorrect_mean = 38
correct_number = 56
incorrect_number = 36

# Find out SUM
incorrect_sum = total_numbers * incorrect_mean 
print(f"Incorrect sum :{incorrect_sum}")

# Correct Sum
diff = correct_number - incorrect_number
correct_sum = incorrect_sum + diff

# Correct mean 
correct_mean = correct_sum / total_numbers
print(f"Coreect mean : {correct_mean}")