amount = int(input("Enter total amount: "))
note_100 = amount//100
note_50 = (amount%100)//50
note_10 = ((amount%100)%50)//10

print("Total '100' rupees notes : ",note_100)
print("Total '50' rupees notes : ",note_50)
print("Total '10' rupees notes : ",note_10)