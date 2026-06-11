print("Choose a shape to calculate area:")
print("1 Rectangle")
print("2 Triangle")
print("3 Circle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print("Area of Rectangle =", area)

elif choice == 2:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = (base * height) / 2
    print("Area of Triangle =", area)

elif choice == 3:
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
