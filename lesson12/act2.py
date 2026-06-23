# Find all prime numbers with in a given range
while True:
    lower = int(input("Enter a lower range : "))
    if lower >= 1:
        break
    print("Invalid input, Enter value greater than 1")

while True:
    upper = int(input("Enter a upper range : "))
    if upper >= lower:
        break
    print(f"Invalid input, Enter value greater than {lower}")

print(f"Prime numbers between {lower } and {upper} are : ")
start =max(2,lower)
for num in range(lower, upper + 1):
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
    