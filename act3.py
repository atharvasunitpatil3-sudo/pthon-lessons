math = int(input("Enter marks of math paper :"))
physics = int(input("Enter marks of physics paper :"))
biology = int(input("Enter marks of biology paper :"))
chemistry = int(input("Enter marks of chemistry paper :"))
english = int(input("Enter marks of english paper :"))

total_marks = math + physics + chemistry + english + biology
print("Sum of marks of all the papers :", total_marks)

your_percentage = (total_marks/500)*100

print(f"Your percentage is : {your_percentage}%")