# To check if any number is divisible by another number

numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

if numerator%denominator == 0:
    print(f"{numerator} is divisible by {denominator}")
else:
    print(f"{numerator} is devisible by{denominator}")