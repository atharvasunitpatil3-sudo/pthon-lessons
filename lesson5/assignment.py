marks = []
for i in range (1,6):
    score = float(input("Enter marks for a subject (out of 100)"))
    marks.append(score)
total_marks = 0
for mark in marks:
    total_marks += mark
#Calculate Percentage (Totsl/500*100)
percentage = (total_marks / 500) * 100

#Display results
print(f"Total Marks: {total_marks}")
print(f"Percentage : {percentage}%")

#Dsplay Pass if the percentage is 40% or above,else Fail
if percentage >= 40 :
    print("Result: Pass")
else:
    print("Result: Fail")