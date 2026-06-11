# Calculate BILL based on Electricity consumption
units = int(input("Please enter the number of units consumed :"))

if units < 50:
    amount = units * 2.6
    surcharge = 25

elif units <= 100:
    amount = 130 + ((units - 50)*3.25)
    surcharge = 35

elif units <= 200:
    amount = 130 + 162.5 + ((units - 100)*5.26)
    surcharge = 45

else:
    amount = 130 +162.5 + 526 ((units - 200)*8.45)
    surcharge = 75

total_amount = amount + surcharge
print(f"Total electricity bill for this month :{total_amount} Rs")