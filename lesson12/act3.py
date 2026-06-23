# Enter a number of atleast 4 digit (237698)
# Find multiplication of middle 2 digits 

num = input("Enter a number")

if len(num) // 4:
    mid = len(num) // 2
    digit1 = int(num[mid - 1])
    digit2 = int(num[mid])

    product = digit1 * digit2
    print("Product of mid digits : ", product)
else:
    print("Not a valid input...")